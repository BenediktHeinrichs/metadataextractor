from .IAdapter import IAdapter


class PrintAdapter(IAdapter):
    def complete(self, text, fileInfo):
        print(text)
        return text

    def complete_metadata(self, metadata, fileInfo):
        return self.complete(metadata, fileInfo)

    def complete_text(self, content, fileInfo):
        return self.complete(content, fileInfo)
