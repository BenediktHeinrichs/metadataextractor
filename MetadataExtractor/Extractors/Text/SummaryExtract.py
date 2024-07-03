from .ITextExtract import ITextExtract
from MetadataExtractor.Util import metadataCreation, metadataFormatter
from transformers import pipeline
import logging

log = logging.getLogger(__name__)


class SummaryExtract(ITextExtract):
    def __init__(self, config):
        ITextExtract.__init__(self, config)
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def text_extract(self, text, fileInfo):
        trig = ""

        if isinstance(text, str) and len(text.strip()) > 30:
            log.info("Executing Summary extraction.")

            formattedSummary = self.summarizer(text, max_length=200, min_length=30, do_sample=False)[0]["summary_text"]

            trig = metadataCreation.addMetadataToFileGraph(
                fileInfo,
                self._IExtract__config,
                {
                    "additionalPrefixes": [
                        "@prefix text: <{}ontologies/text/>".format(
                            metadataFormatter.getBaseUrl(self._IExtract__config)
                        )
                    ],
                    "values": [
                        {"predicate": "text:summarizedBy", "object": formattedSummary}
                    ],
                },
            )

        return trig, "trig"
