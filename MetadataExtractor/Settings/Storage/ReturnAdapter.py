from .IAdapter import IAdapter


class ReturnAdapter(IAdapter):
    def complete(self, text, fileInfo):
        return text

    def complete_metadata(self, metadata, fileInfo):
        return self.complete(metadata, fileInfo)

    def complete_text(self, content, fileInfo):
        return self.complete(content, fileInfo)
