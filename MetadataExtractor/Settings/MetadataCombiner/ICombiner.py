from abc import ABCMeta, abstractmethod


class ICombiner:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def add(self, metadata, metadataformat):
        raise NotImplementedError

    def combine(self, fileInfo):
        combination = self.perform_combine(fileInfo)
        self.reset()
        return combination

    @abstractmethod
    def perform_combine(self, fileInfo):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError
