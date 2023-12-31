from PIL import Image
from PIL.ExifTags import TAGS
import logging
from MetadataExtractor.Util import metadataCreation, metadataFormatter
from .IImageExtract import IImageExtract

log = logging.getLogger(__name__)


class DescriptiveImageExtract(IImageExtract):
    def image_extract(
        self, fileInfo, showDifference=False, rootFileInfo=False, frameNumber=False
    ):
        file = fileInfo["file"]

        config = self._IExtract__config

        log.info('Extracting descriptive information from image "' + file + '".')

        ontology = "image"

        trig = ""

        try:
            image = Image.open(file)

            metadata = {
                "ebucore:height": image.height,
                "ebucore:width": image.width,
                "ebucore:hasFormat": image.format,
                "image:mode": image.mode,
                "image:isAnimated": getattr(image, "is_animated", False),
                "image:frameNumber": getattr(image, "n_frames", 1),
            }

            exifdata = image.getexif()

            # iterating over all EXIF data fields
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)

                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode(errors="ignore")

                if isinstance(data, str) and "\n" in data and "=" in data:
                    for line in data.split("\n"):
                        if "\x01" not in line and "\x17" not in line and "=" in line:
                            kvs = line.split("=")
                            metadata[
                                "image:"
                                + str(metadataFormatter.replaceForbiddenValues(kvs[0]))
                            ] = kvs[1]
                    continue

                metadata["image:" + str(tag)] = data

            metadata = [
                {"predicate": key, "object": value}
                for key, value in metadata.items()
                if value is not None and value != ""
            ]

            trig += metadataCreation.addMetadataToFileGraph(
                fileInfo,
                self._IExtract__config,
                {
                    "additionalPrefixes": [
                        "@prefix ebucore: <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#>",
                        "@prefix {}: <{}ontologies/{}#>".format(
                            ontology,
                            metadataFormatter.getBaseUrl(config),
                            ontology,
                        ),
                    ],
                    "values": metadata,
                },
            )
        except Exception:
            return ("", "")

        return ("", trig)

    def extract(
        self, fileInfo, showDifference=False, rootFileInfo=False, frameNumber=False
    ):
        return self.image_extract(fileInfo, showDifference, rootFileInfo, frameNumber)


if __name__ == "__main__":
    objectExtract = DescriptiveImageExtract({})
    objectExtract.image_extract(
        {"identifier": "1234", "file": ".\\Dump\\fruits.jpeg"}, __debug__
    )
