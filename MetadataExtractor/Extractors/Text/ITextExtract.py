from abc import abstractmethod
from ..Interfaces.IExtract import IExtract
from MetadataExtractor.Util import fileUtil


class ITextExtract(IExtract):
    @abstractmethod
    def text_extract(self, text, fileInfo):
        raise NotImplementedError

    def registerMimeTypes(self):
        # Special case since always called
        self.mimeTypes["matching"] = self._IExtract__emptyMimeTypes()

    def extract(self, fileInfo):
        text = fileUtil.file_extract(fileInfo["file"])
        return self.text_extract(text, fileInfo)
