import logging

log = logging.getLogger(__name__)

from .ICombiner import ICombiner


class BasicCombiner(ICombiner):
    def __init__(self, config):
        ICombiner.__init__(self, config)
        self.reset()

    def add(self, metadata, metadataformat):
        log.info("Adding Metadata to list.")
        self.__metadataEntries.append(metadata)

    def perform_combine(self):
        log.info("Combining Metadata.")
        return "\n".join(self.__metadataEntries)

    def reset(self):
        self.__metadataEntries = []
