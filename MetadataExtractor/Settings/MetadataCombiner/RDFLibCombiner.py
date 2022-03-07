import logging

log = logging.getLogger(__name__)
from rdflib.graph import Graph, ConjunctiveGraph

from .ICombiner import ICombiner


class RDFLibCombiner(ICombiner):
    def __init__(self, config):
        ICombiner.__init__(self, config)
        self.reset()

    def add(self, metadata, metadataformat):
        log.info("Adding Metadata to graph.")
        self.__g.parse(data=metadata, format=metadataformat)

    def perform_combine(self):
        log.info("Combining Metadata.")
        if __debug__:
            persons = []
            locations = []
            dbpedia = []
            dbyago = []
            for (subject, predicate, obj) in self.__g:
                stringObject = str(obj)
                if (
                    "http://www.newsreader-project.eu/ontologies/LOCATION"
                    == stringObject
                ):
                    locations.append(str(subject))
                elif (
                    "http://www.newsreader-project.eu/ontologies/PERSON" == stringObject
                ):
                    persons.append(str(subject))
                elif "http://dbpedia.org/resource/" in stringObject:
                    dbpedia.append(str(stringObject))
                elif "http://dbpedia.org/class/yago/" in stringObject:
                    dbyago.append(str(stringObject))
            log.debug("Persons: " + repr(set(persons)))
            log.debug("Locations: " + repr(set(locations)))
            log.debug("DBpedia entries: " + repr(set(dbpedia)))
            log.debug("DByago entries: " + repr(set(dbyago)))
        return self.__g.serialize(format="trig", encoding="utf-8").decode("utf-8")

    def reset(self):
        self.__g = ConjunctiveGraph()
