from ..Interfaces.IExtract import IExtract


class IPdfExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = ["application/pdf"]
