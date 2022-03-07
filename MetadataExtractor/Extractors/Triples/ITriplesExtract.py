from ..Interfaces.IExtract import IExtract


class ITriplesExtract(IExtract):
    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = [
            "application/rdf+xml",
            "application/n-triples",
            "application/n-quads",
            "text/turtle",
            "text/n3",
        ]
