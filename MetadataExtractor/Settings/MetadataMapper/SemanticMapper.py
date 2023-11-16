from .IMapper import IMapper
import logging
import requests
import json

log = logging.getLogger(__name__)

import os
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib import URIRef, Literal
from MetadataExtractor.Util import metadataCreation

import validators


# TODO: Use SemanticMapper implementation (contact the server ~~or include lib~~)
class SemanticMapper(IMapper):
    def mappingWrapper(self, variableSubjects, config):
        # TODO: Rework Data Holding
        applicationProfiles = []
        for applicationProfile in self.__applicationProfiles:
            applicationProfiles.append(
                {
                    "definition": applicationProfile.serialize(
                        format="turtle", encoding="utf-8"
                    ).decode("utf-8")
                }
            )

        vocabularies = []
        for vocabulary in self.__vocabularies:
            vocabularies.append(
                {
                    "definition": vocabulary.serialize(
                        format="turtle", encoding="utf-8"
                    ).decode("utf-8")
                }
            )

        sendEntries = []
        for variableSubject in variableSubjects:
            entries = variableSubjects[variableSubject]
            currentEntryObject = {}
            for entry in entries:
                currentEntryObject[entry[2]] = entry[3]
            sendEntries.append(currentEntryObject)

        mappingService = config["Values"]["Settings"]["MappingService"]

        response = requests.post(
            mappingService,
            json=json.dumps(
                {
                    "applicationProfiles": applicationProfiles,
                    "vocabularies": vocabularies,
                    "entries": sendEntries,
                }
            ),
        )
        return json.loads(response.text)

    def map(self, metadata, metadataformat="trig"):
        log.info("Mapping metadata values")

        config = self._IMapper__config

        serviceConnection = False
        if (
            "Values" in config
            and "Settings" in config["Values"]
            and "MappingService" in config["Values"]["Settings"]
        ):
            serviceConnection = True

        if not serviceConnection:
            return metadata

        g = ConjunctiveGraph()
        g.parse(data=metadata, format=metadataformat)

        self.__applicationProfiles = []
        if (
            "Values" in config
            and "Settings" in config["Values"]
            and "ApplicationProfiles" in config["Values"]["Settings"]
        ):
            self.__applicationProfiles = self.parseGraphs(
                config["Values"]["Settings"]["ApplicationProfiles"]
            )
        self.__vocabularies = []
        if (
            "Values" in config
            and "Settings" in config["Values"]
            and "Vocabularies" in config["Values"]["Settings"]
        ):
            self.__vocabularies = self.parseGraphs(
                config["Values"]["Settings"]["Vocabularies"]
            )

        attributesUrl = metadataCreation.getOntologyAttributesUrl(config, "mex")
        codeTokenUrl = metadataCreation.getOntologyUrl(config, "codetoken")
        imageUrl = metadataCreation.getOntologyUrl(config, "image")

        variableSubjects = dict()
        for subject, predicate, obj, contextGraph in g.quads():
            predStr = str(predicate)
            if (
                attributesUrl in predStr
                or codeTokenUrl in predStr
                or imageUrl in predStr
            ):
                if subject in variableSubjects:
                    variableSubjects[subject].append(
                        (
                            predicate,
                            obj,
                            self.formatEntity(predicate),
                            self.formatEntity(obj),
                            contextGraph,
                        )
                    )
                else:
                    variableSubjects[subject] = [
                        (
                            predicate,
                            obj,
                            self.formatEntity(predicate),
                            self.formatEntity(obj),
                            contextGraph,
                        )
                    ]

        try:
            mappingCollections = self.mappingWrapper(variableSubjects, config)

            count = 0
            for variableSubject in variableSubjects:
                entries = variableSubjects[variableSubject]
                mappings = mappingCollections[count]
                for entry in entries:
                    partPredicate = entry[2]
                    if partPredicate in mappings:
                        vals = mappings[partPredicate]
                        if vals is not None:
                            predicate = entry[0]
                            obj = str(entry[1])
                            if type(vals) is list:
                                predicate = vals[0]
                                obj = vals[1]
                            else:
                                predicate = vals

                            predicate = self.convertStringToRdflibTerm(predicate)
                            obj = self.convertStringToRdflibTerm(obj)

                            g.remove((variableSubject, entry[0], entry[1], entry[4]))
                            entry[4].add((variableSubject, predicate, obj))
                count += 1
        except requests.exceptions.ConnectionError:
            log.error("SemanticMapping not running")

        self.__applicationProfiles = []
        self.__vocabularies = []

        return g.serialize(format=metadataformat, encoding="utf-8").decode("utf-8")

    def convertStringToRdflibTerm(self, string: str):
        if validators.url(string):
            return URIRef(string)
        else:
            return Literal(string)

    def parseGraphs(self, graphs):
        returnList = []
        currentPath = os.path.dirname(os.path.realpath(__file__))
        for graph in graphs:
            g = Graph()
            if "file" in graph:
                # Don't fail if file does not exist
                try:
                    buildPath = "../../../Data/" + graph["file"]
                    graphPath = os.path.abspath(os.path.join(currentPath, buildPath))
                    g.parse(source=graphPath, format=graph["format"])
                except:
                    log.error("Path not valid: " + graphPath)
            elif "data" in graph:
                g.parse(data=graph["data"], format=graph["format"])
            returnList.append(g)
        return returnList

    def formatEntity(self, entity):
        formattedEntity = str(entity).lower()
        if "#" in formattedEntity:
            formattedEntity = formattedEntity[formattedEntity.rfind("#") + 1 :]
        else:
            formattedEntity = formattedEntity[formattedEntity.rfind("/") + 1 :]
        return formattedEntity
