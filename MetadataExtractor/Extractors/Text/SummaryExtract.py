from .ITextExtract import ITextExtract
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import gensim
from gensim.summarization.textcleaner import (
    clean_text_by_sentences as _clean_text_by_sentences,
)
import logging

log = logging.getLogger(__name__)


class SummaryExtract(ITextExtract):
    def text_extract(self, text, fileInfo):

        sentences = _clean_text_by_sentences(text)
        trig = ""

        if len(sentences) > 1:

            log.info("Executing Summary extraction.")
            gensim_summary = gensim.summarization.summarize(text)

            formattedSummary = gensim_summary.replace("\\", "").replace('"""', "'''")

            trig = metadataCreation.addMetadataToFileGraph(
                fileInfo,
                self._IExtract__config,
                {
                    "additionalPrefixes": [
                        "@prefix text: <{}/ontologies/text/>".format(
                            metadataFormatter.getBaseUrl(self._IExtract__config)
                        )
                    ],
                    "values": [
                        {"predicate": "text:summarizedBy", "object": formattedSummary}
                    ],
                },
            )

        return trig, "trig"
