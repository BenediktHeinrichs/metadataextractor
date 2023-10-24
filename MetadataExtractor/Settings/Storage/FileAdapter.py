import os
import logging

log = logging.getLogger(__name__)

from .IAdapter import IAdapter


class FileAdapter(IAdapter):
    def __init__(self, config):
        IAdapter.__init__(self, config)
        self.__outputPath = "output"
        if (
            "Values" in config
            and "Settings" in config["Values"]
            and "OutputPath" in config["Values"]["Settings"]
            and config["Values"]["Settings"]["OutputPath"]
        ):
            self.__outputPath = config["Values"]["Settings"]["OutputPath"]

    def complete(self, text, fileInfo, extension=".trig"):
        if not os.path.exists(self.__outputPath):
            os.makedirs(self.__outputPath)
        textFile = self.__outputPath + "/" + fileInfo["identifier"].replace("/", "%2F") + extension
        log.info('Storing text to "' + textFile + '".')
        with open(textFile, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        return textFile

    def complete_metadata(self, metadata, fileInfo):
        return self.complete(metadata, fileInfo, "." + self.__config["Values"]["Settings"]["Format"])

    def complete_text(self, content, fileInfo):
        return self.complete(content, fileInfo, ".txt")
