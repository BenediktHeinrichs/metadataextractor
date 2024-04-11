from .IDataExtract import IDataExtract
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import pydicom
from pathlib import Path
from pydicom._version import __version_info__
import logging

log = logging.getLogger(__name__)


class DicomExtract(IDataExtract):
    def extract(self, fileInfo):
        log.info('Extracting metadata for Dicom file "' + fileInfo["file"] + '".')
        text = ""

        dicom_metadata = pydicom.dcmread(file)
        
        for elem in dicom_metadata.iterall():
            if elem.tag.is_private:
                continue  # Skip private tags
            tag_str = str(elem.tag)
            value = elem.value
            if isinstance(value, pydicom.valuerep.DSfloat):
                value = float(value)
            dicom_metadata[tag_str] = value

        values = []
        identifier = fileInfo["identifier"]

        for attribute in dicom_metadata.keys():
            objectValue = dicom_metadata[attribute]
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
        self.mimeTypes["concrete"] = ["application/dcm"]
