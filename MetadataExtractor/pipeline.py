# Usage: Manually run Apache Tika "java -jar tika-server-1.23.jar" and manually run Apache Stanbol
# For better results: Install Tesseract
# Note however that this makes PDF extraction with images much slower

import os
import importlib
import uuid
import logging

log = logging.getLogger(__name__)
import magic
from MetadataExtractor.Util import inputFilter, metadataCreation, mimeTypeFixer

# Dynamic import based on config
def importDependencies(config):
    packageName = "MetadataExtractor"
    for package in ["Extractors", "Refiners", "Settings"]:
        for key, val in config[package].items():
            if not isinstance(val, list):
                val = [val]
            count = 0
            for entry in val:
                module = importlib.import_module(
                    packageName + "." + package + "." + key + "." + entry
                )
                globals().update({entry: module})
                instance = eval(entry + "." + entry + "(config)")
                if isinstance(config[package][key], list):
                    config[package][key][count] = instance
                else:
                    config[package][key] = instance
                count = count + 1


class MetadataHandler:
    def __init__(
        self,
        fileInfo,
        config,
        storageImplementations,
        metadataCombinerImplementations,
        metadataMapperImplementations,
        metadataRefiners={},
    ):
        self.__fileInfo = fileInfo
        self.__config = config
        self.__storageImplementations = storageImplementations
        self.__metadataCombinerImplementations = metadataCombinerImplementations
        self.__metadataMapperImplementations = metadataMapperImplementations
        self.__metadataRefiners = metadataRefiners

    def refine_and_store_metadata(self, metadata, metadataformat="trig", mimetype=None):
        fileInfo = self.__fileInfo
        if (
            mimetype != None
            and mimetype in self.__metadataRefiners
            and len(self.__metadataRefiners[mimetype]) > 0
        ):
            for metadataRefiner in self.__metadataRefiners[mimetype]:
                (
                    changedMetadata,
                    changedMetadataFormat,
                ) = metadataRefiner.refine_metadata(
                    metadata, fileInfo, metadataformat=metadataformat
                )
                for (
                    metadataCombinerImplementation
                ) in self.__metadataCombinerImplementations:
                    metadataCombinerImplementation.add(
                        changedMetadata, changedMetadataFormat
                    )
        else:
            for (
                metadataCombinerImplementation
            ) in self.__metadataCombinerImplementations:
                metadataCombinerImplementation.add(metadata, metadataformat)

    def handleText(self, extractors, text):
        usedType = "Text"
        fileInfo = self.__fileInfo
        for extractor in extractors[usedType]:
            metadata, metadataformat = extractor.text_extract(text, fileInfo)
            self.refine_and_store_metadata(
                metadata, metadataformat=metadataformat, mimetype=usedType
            )

    def complete_storing(self, content):
        metadata = ""
        for metadataCombinerImplementation in self.__metadataCombinerImplementations:
            metadata += metadataCombinerImplementation.combine()
        for metadataMapperImplementation in self.__metadataMapperImplementations:
            metadata = metadataMapperImplementation.map(metadata)
        fileInfo = self.__fileInfo
        returnObject = { "identifier": fileInfo["identifier"] }
        for storageImplementation in self.__storageImplementations:
            returnObject["metadata"] = storageImplementation.complete_metadata(
                metadata, fileInfo
            )
            if self.__config["Values"]["Settings"]["StoreContent"]:
                returnObject["text"] = storageImplementation.complete_text(
                    content, fileInfo
                )
        return returnObject


# This method handles the MetadataExtractor pipeline
# It expects a file array input and a config file
# An example of a config object can be found in "pipeline_runner.py"
def run_pipeline(fileInfos: list, config):

    importDependencies(config)

    resultArray = []

    if config["Values"]["Generic"]["MagicMimeType"]:
        mime = magic.Magic(mime=True)

    for fileInfo in fileInfos:

        if fileInfo["identifier"] == None:
            fileInfo["identifier"] = str(uuid.uuid4()) + "/" + fileInfo["file"][fileInfo["file"].rindex(os.sep)+1:]

        log.info('Starting pipeline on "' + str(fileInfo) + '".')

        isUrl = inputFilter.isUrl(fileInfo["file"])
        if isUrl:
            fileInfo["file"] = inputFilter.downloadFile(fileInfo["file"])

        content = ""

        metadataHandler = MetadataHandler(
            fileInfo,
            config,
            config["Settings"]["Storage"],
            config["Settings"]["MetadataCombiner"],
            config["Settings"]["MetadataMapper"],
            config["Refiners"],
        )

        extractors = config["Extractors"]

        for extractor in extractors["Generic"]:
            generic_extraction = extractor.extract(fileInfo)
            log.debug("The generic extraction result:")
            log.debug(repr(generic_extraction))
            metadataHandler.refine_and_store_metadata(
                generic_extraction, mimetype="Generic"
            )
            # TODO: Somehow merge generic_extractions

        if (
            generic_extraction["content"]
            and not generic_extraction["content"].isspace()
        ):
            content += generic_extraction["content"] + "\n"

        if config["Values"]["Generic"]["MagicMimeType"]:
            generic_extraction["metadata"]["Content-Type"] = mime.from_file(
                fileInfo["file"]
            )
        if type(generic_extraction["metadata"]["Content-Type"]) is list:
            generic_extraction["metadata"]["Content-Type"] = generic_extraction["metadata"]["Content-Type"][0]
        mimetype = generic_extraction["metadata"]["Content-Type"].lower()
        mimetype = mimeTypeFixer.fixMimeType(mimetype)
        log.info("Mimetype: " + repr(mimetype))
        # Store MimeType
        metadataHandler.refine_and_store_metadata(
            metadataCreation.addMetadataToFileGraph(
                fileInfo,
                config,
                {
                    "additionalPrefixes": [
                        "@prefix dcat: <http://www.w3.org/ns/dcat#>"
                    ],
                    "values": [{"predicate": "dcat:mediaType", "object": mimetype}],
                },
                True
            )
        )

        for extractorType in extractors.keys():
            for extractor in extractors[extractorType]:
                if mimetype in extractor.mimeTypes["concrete"] or any(
                    entry.lower() in mimetype
                    for entry in extractor.mimeTypes["matching"]
                ):
                    (text, metadata) = extractor.extract(fileInfo)
                    metadataHandler.refine_and_store_metadata(
                        metadata, mimetype=extractorType
                    )
                    if text and not text.isspace():
                        content += text + "\n"

        # Text extractor will always be run, since most of the time some kind of textual representation can be taken
        if content and not content.isspace():
            metadataHandler.handleText(extractors, content)

        resultArray.append(metadataHandler.complete_storing(content))

        log.info('Finished pipeline on "' + str(fileInfo) + '".')

        if isUrl:
            os.remove(fileInfo["file"])

    return resultArray
