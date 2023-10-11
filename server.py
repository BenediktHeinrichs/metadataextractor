from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, inputs
from werkzeug.datastructures import FileStorage
import os
import uuid
import shutil
import re
import base64
import quopri
from urllib.parse import urlparse
from urllib.request import urlretrieve, urlopen
import filedate
import logging
from defaultConfigs import setDefaultLogging, getDefaultConfig

setDefaultLogging()

log = logging.getLogger(__name__)

from MetadataExtractor.pipeline import run_pipeline
from MetadataExtractor import __version__

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = os.environ.get("MAX_CONTENT_LENGTH", 500 * 1000 * 1000)
api = Api(app, version=__version__, title='Metadata Extractor API',
    description='This API extracts RDF triples from files',
)

def encoded_words_to_text(encoded_words):
    encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
    result = re.match(
        encoded_word_regex, encoded_words
    )
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
parser.add_argument('identifier', type=str, help='File Identifier', location='form')
parser.add_argument('config', type=object, help='Object defining the utilized configuration (try "/defaultConfig" to get the structure)', location='form')
parser.add_argument('creation_date', type=inputs.datetime, help='Creation Date (Time) (e.g. "2022-09-15T09:27:17.3550000+02:00")', location='form')
parser.add_argument('modification_date', type=inputs.datetime, help='Modification Date (Time) (e.g. "2022-09-15T09:27:17.3550000+02:00")', location='form')
parser.add_argument('url', type=str, help='Download URL of file', location='form')
parser.add_argument('file', type=FileStorage, location='files')

metadataOutput = api.model('MetadataOutput', {
    "identifier": fields.String(),
    "metadata": fields.String(),
    "text": fields.String()
})

@api.route("/")
class MetadataExtractorWorker(Resource):
    '''Performs the Metadata Extraction'''
    @api.expect(parser)
    @api.response(200, 'Success', [metadataOutput])
    @api.response(400, 'Bad Request')
    @api.response(413, 'Request Entity Too Large (' + str(app.config['MAX_CONTENT_LENGTH']) + ' maximum)')
    def post(self):

        pipelineInput = []

        data = dict(request.form)
        folder = os.path.join(str(os.getcwd()), str(uuid.uuid4()))
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        if 'file' in request.files:
            fileIdentifier = request.files['file'].filename
            fileName = os.path.join(folder, fileIdentifier)
            dirName = fileName[:fileName.rindex(os.sep)]
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            request.files['file'].save(fileName)
        elif 'url' in data:
            parsedUrl = urlparse(data['url'])
            fileIdentifier = os.path.basename(parsedUrl.path)
            fileName = os.path.join(folder, fileIdentifier)
            dirName = fileName[:fileName.rindex(os.sep)]
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            site = urlopen(data['url'])
            if int(site.getheader("Content-Length")) > app.config['MAX_CONTENT_LENGTH']:
                return "File too big", 400
            urlretrieve(data['url'], fileName)
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
            accessed=get_file_date["accessed"]
        )

        pipelineInput.append({"identifier": identifier, "file": fileName})

        if "config" in data:
            config = data["config"]
        else:
            config = getDefaultConfig()
        if "Settings" not in config:
            config = getDefaultConfig()
        config["Settings"]["Storage"] = ["ReturnAdapter"]

        iterativeList = run_pipeline(pipelineInput, config)

        shutil.rmtree(folder, ignore_errors=True)

        return jsonify(iterativeList)

@api.route("/defaultConfig")
class ConfigWorker(Resource):
    '''Returns the default configuration of the Metadata Extractor'''
    def get(self):
        return jsonify({"config": getDefaultConfig()})

versionModel = api.model('Version', {
    "version": fields.String()
})

@api.route("/version")
class VersionWorker(Resource):
    '''Returns the current version of the Metadata Extractor'''
    @api.response(200, 'Success', versionModel)
    def get(self):
        return jsonify({"version": __version__})

if __name__ == "__main__":
    from waitress import serve
    serve(
        app,
        host=os.environ.get("METADATAEXTRACTORHOST", "0.0.0.0"),
        port=os.environ.get("METADATAEXTRACTORPORT", 36541),
    )
