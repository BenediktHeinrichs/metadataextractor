from ..Interfaces.IExtract import IExtract


class IAudioExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["matching"] = ["Audio"]
