import logging

log = logging.getLogger(__name__)
from rdflib.graph import ConjunctiveGraph

from .ICombiner import ICombiner


class RDFLibCombiner(ICombiner):
    def __init__(self, config):
        ICombiner.__init__(self, config)
        self.reset()

    def add(self, metadata, metadataformat):
        log.info("Adding Metadata to graph.")
        self.__g.parse(data=metadata, format=metadataformat)

    def perform_combine(self, fileInfo):
        log.info("Combining Metadata.")
        return self.__g.serialize(
            format=self._ICombiner__config["Values"]["Settings"]["Format"],
            encoding="utf-8",
        ).decode("utf-8")

    def reset(self):
        self.__g = ConjunctiveGraph()
