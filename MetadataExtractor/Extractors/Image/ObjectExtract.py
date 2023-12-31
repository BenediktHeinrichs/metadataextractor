# https://towardsdatascience.com/object-detection-with-less-than-10-lines-of-code-using-python-2d28eebc5b11
import cv2
import super_gradients
import logging
from collections import Counter
from MetadataExtractor.Util import metadataCreation, metadataFormatter
from .IImageExtract import IImageExtract

log = logging.getLogger(__name__)


class ObjectExtract(IImageExtract):
    def image_extract(self, fileInfo, rootFileInfo=False, frameNumber=False):
        file = fileInfo["file"]

        config = self._IExtract__config

        log.info('Extracting objects from image "' + file + '".')

        text = ""
        trig = ""

        im = cv2.imread(file)
        if im is not None:
            yolo_nas = super_gradients.training.models.get(
                "yolo_nas_l", pretrained_weights="coco"
            )
            model_predictions = yolo_nas.predict(file)
            model_prediction = model_predictions[0]
            all_class_names = model_prediction.class_names
            prediction = model_prediction.prediction

            labels = prediction.labels
            class_names = {}
            for label in labels:
                labelint = int(label)
                class_name = all_class_names[labelint]
                if class_name in class_names:
                    class_names[class_name] += 1
                else:
                    class_names[class_name] = 1

            counter = Counter(class_names)

            ontology = "image"

            if rootFileInfo is not False:
                fileIdentifier = metadataFormatter.formatIdentifier(
                    fileInfo["identifier"]
                )

                trig += metadataCreation.addMetadataToFileGraph(
                    rootFileInfo,
                    config,
                    {
                        "values": [
                            {
                                "predicate": "foaf:depiction",
                                "object": "{}ontologies/graph/{}".format(
                                    metadataFormatter.getBaseUrl(config), fileIdentifier
                                ),
                            },
                        ]
                    },
                )

                if frameNumber is not False:
                    trig += metadataCreation.addMetadataToFileGraph(
                        fileInfo,
                        self._IExtract__config,
                        {
                            "additionalPrefixes": [
                                "@prefix {}: <{}ontologies/{}#>".format(
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

            for elemn, cnt in counter.items():
                obj = "{}ontologies/{}/object#{}".format(
                    metadataFormatter.getBaseUrl(config),
                    ontology,
                    metadataFormatter.replaceForbiddenValues(elemn),
                )
                trig += metadataCreation.addMetadataToFileGraph(
                    fileInfo,
                    self._IExtract__config,
                    {
                        "additionalPrefixes": [
                            "@prefix {}object: <{}ontologies/{}/object#>".format(
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

            if len(class_names) > 0:
                text += (
                    "This image"
                    + (
                        " on frame " + str(frameNumber)
                        if frameNumber is not False
                        else ""
                    )
                    + " contains "
                )
                for elemn, cnt in counter.items():
                    text += str(cnt) + " " + elemn + ", "
                text = text[:-2]
                text += " as objects."
            log.debug(text)
        return ("", trig)

    def extract(self, fileInfo, rootFileInfo=False, frameNumber=False):
        return self.image_extract(fileInfo, rootFileInfo, frameNumber)


if __name__ == "__main__":
    objectExtract = ObjectExtract({})
    objectExtract.image_extract(
        {"identifier": "1234", "file": ".\\Examples\\fruits.jpeg"}
    )
