# Requirement: https://stanbol.apache.org/docs/trunk/tutorial.html
import requests
from ..Interfaces.IRefine import IRefine


class StanbolRefine(IRefine):
    def __init__(self, config):
        IRefine.__init__(self, config)
        self.__url = "http://localhost:8080/enhancer/engine/tika"

    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):
        result = None
        with open(fileInfo["file"], "rb") as payload:
            data = payload.read()
            headers = {
                "Accept": "application/rdf+xml",
                "Content-Type": "application/octet-stream",
            }
            result = requests.post(self.__url, data=data, headers=headers)
        return (result.text, "xml")
