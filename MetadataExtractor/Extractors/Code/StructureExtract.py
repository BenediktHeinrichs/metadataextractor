from .ICodeExtract import ICodeExtract

from pygments import lex
from pygments.lexers import guess_lexer_for_filename
from pygments.token import Name

import logging

from MetadataExtractor.Util import metadataCreation, metadataFormatter

log = logging.getLogger(__name__)


class StructureExtract(ICodeExtract):
    def extract(self, fileInfo):
        with open(fileInfo["file"], "r", encoding="utf-8") as content_file:
            code = content_file.read()

        try:
            lexer = guess_lexer_for_filename(fileInfo["file"], code)
        except Exception:
            return ("", "")

        log.info("Extracting structural metadata with pygments.")

        values = []
        for token in lex(code, lexer):
            if token[0] in Name:
                tokenName = str(token[0]).replace("Token.", "")
                tokenValue = token[1]

                predicate = "codetoken:" + tokenName.replace(".", "_")
                values.append({"predicate": predicate, "object": tokenValue})

        return (
            "",
            metadataCreation.addMetadataToFileGraph(
                fileInfo,
                self._IExtract__config,
                {
                    "additionalPrefixes": [
                        "@prefix codetoken: <{}ontologies/codetoken#>".format(
                            metadataFormatter.getBaseUrl(self._IExtract__config)
                        )
                    ],
                    "values": values,
                },
            ),
        )
