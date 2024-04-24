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

        dicom_metadata = pydicom.dcmread(fileInfo["file"])
        
        for elem in dicom_metadata.iterall():
            if elem.tag.is_private:
                continue  # Skip private tags
            tag_str = elem.tag
            value = elem.value
            if isinstance(value, pydicom.valuerep.DSfloat):
                value = float(value)
            logging.info(dicom_metadata.keys)
                # Construct a DataElement instance
            data_element = pydicom.DataElement(tag_str, elem.VR, value)
            dicom_metadata[tag_str] = data_element

        values = []
        identifier = fileInfo["identifier"]

        for attribute in dicom_metadata.keys():
            objectValue = dicom_metadata[attribute]
            values.append(
                {
                    "predicate": "mexattr:" + metadataFormatter.replaceForbiddenValues(str(attribute)),
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
        self.mimeTypes["concrete"] = ["application/dcm", "application/dicom"]
