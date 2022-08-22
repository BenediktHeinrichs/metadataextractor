from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage
import os
import uuid
import shutil
import re
import base64
import quopri
import json
import logging
from defaultConfigs import setDefaultLogging, getDefaultConfig

setDefaultLogging()

log = logging.getLogger(__name__)

from MetadataExtractor.pipeline import run_pipeline
from MetadataExtractor import __version__

app = Flask(__name__)
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
parser.add_argument('files', type=FileStorage, location='files')

metadataOutput = api.model('Metadata Output', { 
    "metadata": fields.String(), 
    "text": fields.String() 
})

mainModel = api.model('Metadata Extraction Result', {
    "identifier1": fields.List(fields.Nested(metadataOutput)),
    "identifier2": fields.List(fields.Nested(metadataOutput)),
    "identifier3": fields.List(fields.Nested(metadataOutput)),
    "...": fields.List(fields.Nested(metadataOutput)),
})

@api.route("/")
class MetadataExtractorWorker(Resource):
    '''Performs the Metadata Extraction'''
    @api.expect(parser)
    @api.response(200, 'Success', [mainModel])
    def post(self):

        pipelineInput = []

        data = dict(request.form)
        folder = os.path.join(str(os.getcwd()), str(uuid.uuid4()))
        if not os.path.exists(folder):
            os.makedirs(folder)
        for file in request.files:
            if file == None:
                fileIdentifier = request.files[file].filename
            else:
                fileIdentifier = encoded_words_to_text(file)
            fileName = os.path.join(folder, fileIdentifier)
            dirName = fileName[:fileName.rindex(os.sep)]
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            request.files[file].save(fileName)
            if "identifier" in data:
                if isinstance(data["identifier"], str):
                    data["identifier"] = json.loads(data["identifier"])
                identifier = data["identifier"][fileIdentifier]
            else:
                identifier = None
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
