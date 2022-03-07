from ..Interfaces.IExtract import IExtract
from pygments.lexers import get_all_lexers


class ICodeExtract(IExtract):
    def registerMimeTypes(self):
        codeMimeTypes = []
        for lexer in get_all_lexers():
            codeMimeTypes += lexer[3]
        self.mimeTypes["concrete"] = codeMimeTypes
