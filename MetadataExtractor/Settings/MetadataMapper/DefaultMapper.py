from .IMapper import IMapper
import logging

log = logging.getLogger(__name__)


class DefaultMapper(IMapper):
    def map(self, metadata, metadataformat="trig"):
        return metadata
