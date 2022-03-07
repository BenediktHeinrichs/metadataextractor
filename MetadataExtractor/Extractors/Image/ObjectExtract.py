# https://towardsdatascience.com/object-detection-with-less-than-10-lines-of-code-using-python-2d28eebc5b11
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
import logging

log = logging.getLogger(__name__)
from collections import Counter
from MetadataExtractor.Util import metadataCreation, metadataFormatter
from ..Interfaces.IExtract import IExtract
from .IImageExtract import IImageExtract


class ObjectExtract(IImageExtract):
    def image_extract(
        self, fileInfo, showDifference=False, rootFileInfo=False, frameNumber=False
    ):

        file = fileInfo["file"]

        config = self._IExtract__config

        log.info('Extracting objects from image "' + file + '".')

        text = ""
        trig = ""

        im = cv2.imread(file)
        if im is not None:
            bbox, labels, conf = cv.detect_common_objects(im)
            if showDifference:
                output_image = draw_bbox(im, bbox, labels, conf)
                plt.imshow(output_image)
                plt.show()

            counter = Counter(labels)

            ontology = "image"

            if rootFileInfo != False:

                fileIdentifier = metadataFormatter.formatIdentifier(
                    fileInfo["identifier"]
                )

                trig += metadataCreation.addMetadataToFileGraph(
                    rootFileInfo["identifier"],
                    config,
                    {
                        "values": [
                            {
                                "predicate": "foaf:depiction",
                                "object": "{}/ontologies/graph/{}".format(
                                    metadataFormatter.getBaseUrl(config), fileIdentifier
                                ),
                            },
                        ]
                    },
                )

                if frameNumber != False:
                    trig += metadataCreation.addMetadataToFileGraph(
                        fileInfo["identifier"],
                        self._IExtract__config,
                        {
                            "additionalPrefixes": [
                                "@prefix {}: <{}/ontologies/{}#>".format(
                                    ontology,
                                    metadataFormatter.getBaseUrl(config),
                                    ontology,
                                )
                            ],
                            "values": [
                                {
                                    "predicate": "{}:frameNumber".format(ontology),
                                    "object": frameNumber,
                                },
                            ],
                        },
                    )

            for (elemn, cnt) in counter.items():
                obj = "{}/ontologies/{}/object#{}".format(
                    metadataFormatter.getBaseUrl(config),
                    ontology,
                    metadataFormatter.replaceForbiddenValues(elemn),
                )
                trig += metadataCreation.addMetadataToFileGraph(
                    fileInfo["identifier"],
                    self._IExtract__config,
                    {
                        "additionalPrefixes": [
                            "@prefix {}object: <{}/ontologies/{}/object#>".format(
                                ontology, metadataFormatter.getBaseUrl(config), ontology
                            )
                        ],
                        "values": [
                            {"predicate": "foaf:depicts", "object": obj},
                            {
                                "subject": obj,
                                "predicate": "{}object:count".format(ontology),
                                "object": cnt,
                            },
                            {
                                "subject": obj,
                                "predicate": "rdfs:label",
                                "object": elemn,
                            },
                        ],
                    },
                )

            if len(labels) > 0:
                text += (
                    "This image"
                    + (" on frame " + str(frameNumber) if frameNumber != False else "")
                    + " contains "
                )
                for (elemn, cnt) in counter.items():
                    text += str(cnt) + " " + elemn + ", "
                text = text[:-2]
                text += " as objects."
            log.debug(text)
        return ("", trig)

    def extract(
        self, fileInfo, showDifference=False, rootFileInfo=False, frameNumber=False
    ):
        return self.image_extract(fileInfo, showDifference, rootFileInfo, frameNumber)


if __name__ == "__main__":

    objectExtract = ObjectExtract({})
    objectExtract.image_extract(
        {"identifier": "1234", "file": ".\\Dump\\fruits.jpeg"}, __debug__
    )
