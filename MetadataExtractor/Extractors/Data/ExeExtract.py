from .IDataExtract import IDataExtract
import pefile
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import logging

log = logging.getLogger(__name__)

class ExeExtract(IDataExtract):
    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = "application/x-msdownload"

    def extract(self, fileInfo):
        log.info('Extracting metadata from exe file: ' + fileInfo["file"])
        pe = pefile.PE(fileInfo["file"])

        # Initialize metadata list
        values = []

        # Add DOS Header metadata
        values.append({"predicate": "exe:e_magic", "object": hex(pe.DOS_HEADER.e_magic)})
        values.append({"predicate": "exe:e_cblp", "object": pe.DOS_HEADER.e_cblp})

        # Add File Header metadata
        values.append({"predicate": "exe:machine", "object": hex(pe.FILE_HEADER.Machine)})
        values.append({"predicate": "exe:numberOfSections", "object": pe.FILE_HEADER.NumberOfSections})

        # Add Optional Header metadata
        values.append({"predicate": "exe:addressOfEntryPoint", "object": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)})
        values.append({"predicate": "exe:imageBase", "object": hex(pe.OPTIONAL_HEADER.ImageBase)})

        # Add Sections metadata
        for section in pe.sections:
            section_values = [
                {"predicate": "exe:sectionName", "object": section.Name.decode().strip()},
                {"predicate": "exe:virtualSize", "object": section.Misc_VirtualSize},
                {"predicate": "exe:virtualAddress", "object": section.VirtualAddress}
            ]
            values.extend(section_values)

        # Additional metadata can be added here

        # Create graph options
        graphOptions = {
            "additionalPrefixes": ["@prefix exe: <{}ontologies/exe#>".format(
                metadataFormatter.getBaseUrl(self._IExtract__config)
            )],
            "identifier": fileInfo["identifier"],
            "ontology": "exe",
            "values": values
        }

        # Add metadata to graph
        metadata = metadataCreation.addEntryToFileGraph(fileInfo, self._IExtract__config, graphOptions)

        return "", metadata
