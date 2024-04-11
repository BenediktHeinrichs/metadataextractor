from ..Interfaces.IExtract import IExtract


class IDataExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = ["text/csv", "text/xml", "application/json"]
