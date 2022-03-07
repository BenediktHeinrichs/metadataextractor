from flask import Flask, request, jsonify
import os
import tempfile
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
from MetadataExtractor.Util import inputFilter
from MetadataExtractor import __version__

app = Flask(__name__)


def encoded_words_to_text(encoded_words):
    encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
    result = re.match(
        encoded_word_regex, encoded_words
    )
    if result:
        charset, encoding, encoded_text = result.groups()
        if encoding is "B":
            byte_string = base64.b64decode(encoded_text)
        elif encoding is "Q":
            byte_string = quopri.decodestring(encoded_text)
        if byte_string:
            byte_string.decode(charset)
    return encoded_words


@app.route("/", methods=["POST"])
def index():

    pipelineInput = []

    data = dict(request.form)
    folder = ".\\" + str(uuid.uuid4())
    if not os.path.exists(folder):
        os.makedirs(folder)
    for file in request.files:
        if file == None:
            fileIdentifier = request.files[file].filename
        else:
            fileIdentifier = encoded_words_to_text(file)
        fileName = folder + "\\" + fileIdentifier
        dirName = os.path.dirname(fileName)
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


@app.route("/defaultConfig", methods=["GET"])
def defaultConfig():
    return jsonify({"config": getDefaultConfig()})


@app.route("/version", methods=["GET"])
def version():
    return jsonify({"version": __version__})


if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.environ.get("METADATAEXTRACTORHOST", "127.0.0.1"),
        port=os.environ.get("METADATAEXTRACTORPORT", 36541),
    )
