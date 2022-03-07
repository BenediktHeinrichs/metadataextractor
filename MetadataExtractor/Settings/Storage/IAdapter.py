from abc import ABCMeta, abstractmethod


class IAdapter:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def complete(self, text, fileInfo):
        raise NotImplementedError

    @abstractmethod
    def complete_metadata(self, metadata, fileInfo):
        raise NotImplementedError

    @abstractmethod
    def complete_text(self, content, fileInfo):
        raise NotImplementedError
