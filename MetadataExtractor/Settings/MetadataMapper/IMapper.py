from abc import ABCMeta, abstractmethod


class IMapper:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def map(self, metadata, metadataformat="trig"):
        raise NotImplementedError
