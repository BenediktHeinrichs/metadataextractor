from abc import ABCMeta, abstractmethod


class IExtract:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.__config = config
        self.mimeTypes = self.__emptyMimeTypes()
        self.registerMimeTypes()

    def __emptyMimeTypes(self):
        return {"concrete": [], "matching": []}

    @abstractmethod
    def registerMimeTypes(self):
        raise NotImplementedError

    @abstractmethod
    def extract(self, fileInfo):
        raise NotImplementedError
