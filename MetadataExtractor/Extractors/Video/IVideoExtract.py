from ..Interfaces.IExtract import IExtract


class IVideoExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["matching"] = ["Video"]
