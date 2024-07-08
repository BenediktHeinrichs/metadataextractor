from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_restx import Api, Resource, fields, inputs
from werkzeug.datastructures import FileStorage
import os
import uuid
import shutil
import re
import base64
import quopri
import json
from urllib.parse import urlparse
from urllib.request import urlretrieve, urlopen
from playwright.sync_api import sync_playwright
import filedate
import logging
from defaultConfigs import setDefaultLogging, getDefaultConfig

from MetadataExtractor.pipeline import run_pipeline
from MetadataExtractor import __version__

setDefaultLogging()

log = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app) # Enables CORS for all routes
app.config["MAX_CONTENT_LENGTH"] = os.environ.get(
    "MAX_CONTENT_LENGTH", 500 * 1000 * 1000
)
api = Api(
    app,
    version=__version__,
    title="Metadata Extractor API",
    description="This API extracts RDF triples from files",
)


def encoded_words_to_text(encoded_words):
    encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
    result = re.match(encoded_word_regex, encoded_words)
    if result:
        charset, encoding, encoded_text = result.groups()
        if encoding == "B":
            byte_string = base64.b64decode(encoded_text)
        elif encoding == "Q":
            byte_string = quopri.decodestring(encoded_text)
        if byte_string:
            byte_string.decode(charset)
    return encoded_words


parser = api.parser()
parser.add_argument("identifier", type=str, help="File Identifier", location="form")
parser.add_argument(
    "config",
    type=object,
    help='Object defining the overwriting configuration (try "/defaultConfig" to get the structure)',
    location="form",
)
parser.add_argument(
    "creation_date",
    type=inputs.datetime,
    help='Creation Date (Time) (e.g. "2022-09-15T09:27:17.3550000+02:00")',
    location="form",
)
parser.add_argument(
    "modification_date",
    type=inputs.datetime,
    help='Modification Date (Time) (e.g. "2022-09-15T09:27:17.3550000+02:00")',
    location="form",
)
parser.add_argument("url", type=str, help="Download URL of file", location="form")
parser.add_argument("dynamic_url", type=str, help="Dynamic download URL of file (JavaScript)", location="form")
parser.add_argument("file", type=FileStorage, location="files")
parser.add_argument(
    "accept",
    required=True,
    location="headers",
    choices=[
        "application/json",
        "application/ld+json",
        "application/rdf+xml",
        "application/trig",
        "text/turtle",
    ],
    default="application/json",
)

metadataOutput = api.model(
    "MetadataOutput",
    {
        "identifier": fields.String(),
        "metadata": fields.String(),
        "text": fields.String(),
    },
)

# From https://stackoverflow.com/a/7205672
def mergedicts(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(mergedicts(dict1[k], dict2[k])))
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])

def writeDynamicUrlToSystem(dynamicUrl, fileName):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(dynamicUrl)
        with open(fileName, 'w') as file:
            file.write(page.content())

@api.route("/")
class MetadataExtractorWorker(Resource):
    """Performs the Metadata Extraction"""

    @api.expect(parser)
    @api.response(200, "Success", [metadataOutput])
    @api.response(400, "Bad Request")
    @api.response(
        413,
        "Request Entity Too Large ("
        + str(app.config["MAX_CONTENT_LENGTH"])
        + " maximum)",
    )
    def post(self):
        try:
            pipelineInput = []

            data = dict(request.form)
            folder = os.path.join(str(os.getcwd()), str(uuid.uuid4()))
            if not os.path.exists(folder):
                os.makedirs(folder)

            if "file" in request.files:
                fileIdentifier = request.files["file"].filename
                fileName = os.path.join(folder, fileIdentifier)
                dirName = fileName[: fileName.rindex(os.sep)]
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                request.files["file"].save(fileName)
            elif "url" in data:
                parsedUrl = urlparse(data["url"])
                fileIdentifier = os.path.basename(parsedUrl.path)
                fileName = os.path.join(folder, fileIdentifier)
                dirName = fileName[: fileName.rindex(os.sep)]
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                site = urlopen(data["url"])
                if int(site.getheader("Content-Length")) > app.config["MAX_CONTENT_LENGTH"]:
                    return "File too big", 400
                urlretrieve(data["url"], fileName)
            elif "dynamic_url" in data:
                parsedUrl = urlparse(data["dynamic_url"])
                fileIdentifier = os.path.basename(parsedUrl.path)
                fileName = os.path.join(folder, fileIdentifier)
                dirName = fileName[: fileName.rindex(os.sep)]
                if not os.path.exists(dirName):
                    os.makedirs(dirName)

                writeDynamicUrlToSystem(data["dynamic_url"], fileName)
            else:
                return "No file sent", 400

            file_date = filedate.File(fileName)
            get_file_date = file_date.get()

            if "identifier" in data:
                identifier = data["identifier"]
            else:
                identifier = None

            if "creation_date" in data:
                creation_date = data["creation_date"]
            else:
                creation_date = get_file_date["created"]

            if "modification_date" in data:
                modification_date = data["modification_date"]
            else:
                modification_date = get_file_date["modified"]

            file_date.set(
                created=creation_date,
                modified=modification_date,
                accessed=get_file_date["accessed"],
            )

            pipelineInput.append({"identifier": identifier, "file": fileName})

            if "config" in data:
                config = dict(mergedicts(getDefaultConfig(), json.loads(data["config"])))
            else:
                config = getDefaultConfig()
            if "Settings" not in config:
                config = getDefaultConfig()
            config["Settings"]["Storage"] = ["ReturnAdapter"]

            mimeType = request.accept_mimetypes.best
            if mimeType == "text/turtle":
                config["Values"]["Settings"]["Format"] = "turtle"
            elif mimeType == "application/ld+json":
                config["Values"]["Settings"]["Format"] = "json-ld"
            elif mimeType == "application/rdf+xml":
                config["Values"]["Settings"]["Format"] = "xml"
            elif mimeType == "application/trig":
                config["Values"]["Settings"]["Format"] = "trig"

            iterativeList = run_pipeline(pipelineInput, config)

            if mimeType == "application/json":
                return jsonify(iterativeList)
            else:
                return Response(iterativeList[0]["metadata"], mimetype=mimeType)
        
        # Delete file, even on error
        finally:
            shutil.rmtree(folder, ignore_errors=True)


@api.route("/defaultConfig")
class ConfigWorker(Resource):
    """Returns the default configuration of the Metadata Extractor"""

    def get(self):
        return jsonify({"config": getDefaultConfig()})


versionModel = api.model("Version", {"version": fields.String()})


@api.route("/version")
class VersionWorker(Resource):
    """Returns the current version of the Metadata Extractor"""

    @api.response(200, "Success", versionModel)
    def get(self):
        return jsonify({"version": __version__})


if __name__ == "__main__":
    from waitress import serve

    serve(
        app,
        host=os.environ.get("METADATA_EXTRACTOR_HOST", "0.0.0.0"),
        port=os.environ.get("METADATA_EXTRACTOR_PORT", 36541),
    )
