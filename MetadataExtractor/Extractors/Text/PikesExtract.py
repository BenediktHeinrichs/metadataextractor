# encoding=utf8
import os
import sys
import urllib
import logging

log = logging.getLogger(__name__)
from argparse import ArgumentParser
import requests
import wget
from nltk.tokenize import sent_tokenize

from MetadataExtractor.Util import fileUtil
from MetadataExtractor.Refiners.Text import PikesRefine
from .ITextExtract import ITextExtract


class PikesParser:
    def __init__(self, pikesApiPoint, pikesBatchSize):
        self.__pikesApiPoint = pikesApiPoint
        self.__pikesBatchSize = pikesBatchSize
        self.__savedResults = []

    def __repr__(self):
        return self.__pikesApiPoint

    def makerequest(self, text):
        payload = {"text": text.replace(u"\u000c", "")}
        return self.__represent(requests.post(self.__pikesApiPoint, data=payload))

    def parse(self, text):
        try:
            if text != None:
                sentences = sent_tokenize(text)
                if len(sentences) > self.__pikesBatchSize:
                    log.info(
                        "Passing the text of "
                        + str(len(sentences))
                        + " sentences in batches of "
                        + str(self.__pikesBatchSize)
                        + " sentences to Pikes"
                    )
                    count = 0
                    metadata = ""
                    while count + self.__pikesBatchSize < len(sentences):
                        log.info(
                            "Passing "
                            + str(count)
                            + " - "
                            + str(count + self.__pikesBatchSize)
                            + " to Pikes"
                        )
                        batch = sentences[count : count + self.__pikesBatchSize]
                        count += self.__pikesBatchSize
                        metadata += "\n" + self.makerequest("\n".join(batch))
                    log.info("Passing the last entries to Pikes")
                    lastBatch = sentences[count:]
                    metadata += "\n" + self.makerequest("\n".join(lastBatch))
                    return metadata
                else:
                    return self.makerequest(text)
            else:
                return ""
        except requests.exceptions.ConnectionError:
            log.error("Pikes not running")
            return ""

    def parseAndSave(self, text):
        res = self.parse(text)
        self.__savedResults.append(res)
        return res

    def __represent(self, result):
        return result.text

    def __iter__(self):
        return self.__savedResults.__iter__()

    @property
    def savedItems(self):
        return len(self.__savedResults)


class PikesExtract(ITextExtract):
    def __init__(self, config):
        ITextExtract.__init__(self, config)
        if (
            "Values" in config
            and "Text" in config["Values"]
            and "PikesApiPoint" in config["Values"]["Text"]
        ):
            givenPikesApiPoint = config["Values"]["Text"]["PikesApiPoint"]
        else:
            givenPikesApiPoint = (
                "https://knowledgestore2.fbk.eu/pikes-demo/api/text2rdf"
            )
        if (
            "Values" in config
            and "Text" in config["Values"]
            and "PikesBatchSize" in config["Values"]["Text"]
        ):
            pikesBatchSize = int(config["Values"]["Text"]["PikesBatchSize"])
        else:
            pikesBatchSize = 100
        self.__givenPikesApiPoint = givenPikesApiPoint
        self.__pikesBatchSize = pikesBatchSize

    def text_extract(self, text, fileInfo=None):
        config = self._IExtract__config
        log.info("Executing Pikes extraction.")
        log.debug("Logging received text:")
        log.debug(text)
        pikesParser = PikesParser(self.__givenPikesApiPoint, self.__pikesBatchSize)
        metadata = pikesParser.parse(text)
        metadataformat = "trig"
        if (
            "Values" in config
            and "Text" in config["Values"]
            and "RefinePikesAutomatically" in config["Values"]["Text"]
        ):
            if config["Values"]["Text"]["RefinePikesAutomatically"]:
                pikesRefine = PikesRefine.PikesRefine(config)
                metadata, metadataformat = pikesRefine.refine_metadata(
                    metadata, fileInfo, skip=False
                )
        return metadata, metadataformat


if __name__ == "__main__":

    def __parse_arguments():
        arg_parser = ArgumentParser()

        arg_parser.add_argument("--file", dest="file", required=True)
        arg_parser.add_argument("--pikesApiPoint", dest="pikesApiPoint", required=False)

        return arg_parser, arg_parser.parse_args()

    args_parser, args = __parse_arguments()

    if len(sys.argv) == 1:
        args_parser.print_help()
        sys.exit(1)

    if args.pikesApiPoint == None:
        pikesExtract = PikesExtract({})
        result = pikesExtract.extract({"identifier": "TestFile", "file": args.file})
    else:
        pikesExtract = PikesExtract({}, args.pikesApiPoint)
        result = pikesExtract.extract({"identifier": "TestFile", "file": args.file})
