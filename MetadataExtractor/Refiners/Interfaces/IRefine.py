from abc import ABCMeta, abstractmethod


class IRefine:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):
        raise NotImplementedError
