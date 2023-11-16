from .IDataExtract import IDataExtract
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import flowkit as fk
import logging

log = logging.getLogger(__name__)


class FcsExtract(IDataExtract):
    def extract(self, fileInfo):
        log.info('Extracting metadata for fcs file "' + fileInfo["file"] + '".')
        text = ""

        fcs_data = fk.Sample(fileInfo["file"])
        attributes = fcs_data.get_metadata()

        values = []
        identifier = fileInfo["identifier"]

        for attribute in attributes.keys():
            objectValue = attributes[attribute]
            values.append(
                {
                    "predicate": "mexattr:"
                    + metadataFormatter.replaceForbiddenValues(attribute),
                    "object": objectValue,
                }
            )

        metadata = metadataCreation.addEntryToFileGraph(
            fileInfo,
            self._IExtract__config,
            {
                "additionalPrefixes": [
                    "@prefix dcat: <http://www.w3.org/ns/dcat#>",
                    "@prefix dcterms: <http://purl.org/dc/terms/>",
                ],
                "identifier": identifier,
                "ontology": "mex",
                "values": values,
            },
        )

        return (text, metadata)

    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = ["application/fcs"]
