from ..Interfaces.IExtract import IExtract


class IGenericExtract(IExtract):
    def registerMimeTypes(self):
        # Special case since always called
        self.mimeTypes = self._IExtract__emptyMimeTypes()
