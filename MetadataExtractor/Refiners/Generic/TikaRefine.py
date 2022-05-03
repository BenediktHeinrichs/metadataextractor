import os
import datetime
import logging

log = logging.getLogger(__name__)
from MetadataExtractor.Util import metadataCreation, metadataFormatter
from ..Interfaces.IRefine import IRefine

class TikaRefine(IRefine):
    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):

        log.info("Refining Tika metadata.")

        # TODO: Make use of http://oscaf.sourceforge.net/nfo.html

        predicatemap = {
            "resourceName": "dcterms:identifier",
            "Content_Type": "dcterms:format",
            "File_Size": "dcat:byteSize",
            "File_Modified_Date": "dcterms:modified",
        }

        skippedValues = ["File_Name"]

        values = []
        
        for (key, value) in metadata["metadata"].items():

            refinedKey = metadataFormatter.replaceForbiddenValues(key)

            if refinedKey in skippedValues:
                continue

            queue = [value]

            while queue != []:
                currentVal = queue.pop()
                if type(currentVal) == list:
                    for entry in currentVal:
                        queue.append(entry)
                    continue
                elif type(currentVal) != str:
                    currentVal = currentVal.decode("utf-8")
                elif "'" in currentVal:
                    currentVal = currentVal[
                        currentVal.find("'") + 1 : currentVal.rfind("'")
                    ]

                if "dc:" in refinedKey or "dcterms:" in refinedKey:
                    values.append({"predicate": refinedKey, "object": currentVal})
                elif refinedKey in predicatemap:
                    values.append({"predicate": predicatemap[refinedKey], "object": currentVal})
                else:
                    values.append(
                        {
                            "predicate": "tika:{}".format(refinedKey),
                            "object": currentVal,
                        }
                    )
        
        values.append({"predicate": "a", "object": "http://www.w3.org/ns/dcat#Catalog"})
        values.append({"predicate": "a", "object": "http://www.w3.org/ns/dcat#Distribution"})

        file_stats = os.stat(fileInfo["file"])

        values.append({"predicate": "dcat:byteSize", "object": file_stats.st_size})
        values.append({"predicate": "dcterms:created", "object": datetime.datetime.fromtimestamp(file_stats.st_ctime)})
        values.append({"predicate": "dcterms:modified", "object": datetime.datetime.fromtimestamp(file_stats.st_mtime)})

        trig = metadataCreation.addMetadataToFileGraph(
            fileInfo["identifier"],
            self._IRefine__config,
            {
                "additionalPrefixes": [
                    "@prefix tika: <{}/ontologies/tika/>".format(
                        metadataFormatter.getBaseUrl(self._IRefine__config)
                    ),
                    "@prefix dcat: <http://www.w3.org/ns/dcat#>"
                ],
                "values": values,
            },
            True
        )

        return (trig, "trig")
