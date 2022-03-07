from ..Interfaces.IRefine import IRefine


class ImageRefine(IRefine):
    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):
        return (metadata, metadataformat)
