from ..Interfaces.IRefine import IRefine


class StructureRefine(IRefine):
    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):
        return (metadata, "trig")
