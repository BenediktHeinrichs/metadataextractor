from ..Interfaces.IExtract import IExtract


class IImageExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["matching"] = ["Image"]
