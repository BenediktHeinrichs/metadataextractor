from sklearn.decomposition import LatentDirichletAllocation as LDA, NMF
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import uuid
import logging
from MetadataExtractor.Util import (
    metadataCreation,
    metadataFormatter,
    pyLDAvisSklearn,
)
import pyLDAvis
import os
from .ITextExtract import ITextExtract

log = logging.getLogger(__name__)


class DetailedTopicExtract(ITextExtract):
    # Helper function
    def print_topics(self, model, vectorizer, number_words):
        topic_text = ""
        words = vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(model.components_):
            topic_text += ("\nTopic #%d:" % topic_idx) + "\n"
            topic_text += (
                '["'
                + (
                    '", "'.join(
                        [words[i] for i in topic.argsort()[: -number_words - 1 : -1]]
                    )
                )
                + '"]\n'
            )
        return topic_text

    def text_extract(self, text, fileInfo):
        config = self._IExtract__config

        metadata = ""

        if text and not text.isspace() and len(text.strip()) > 5:
            log.info("Executing topic extraction.")

            # TODO: Implement detecting the optimal numbers:
            # https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/#17howtofindtheoptimalnumberoftopicsforlda
            number_topics = int(config["Values"]["Text"]["NumberOfTopics"])
            number_words = int(config["Values"]["Text"]["NumberOfWords"])

            if config["Values"]["Text"]["Vectorizer"] == "Count":
                vectorizer = CountVectorizer(stop_words="english")
            elif config["Values"]["Text"]["Vectorizer"] == "Tfidf":
                vectorizer = TfidfVectorizer(stop_words="english")
            else:
                raise KeyError(
                    'config["Values"]["Text"]["Vectorizer"] was not specified'
                )
            data = vectorizer.fit_transform(text.split("\n"))

            if config["Values"]["Text"]["TopicExtractor"] == "LDA":
                model = LDA(n_components=number_topics, n_jobs=-1)
            elif config["Values"]["Text"]["TopicExtractor"] == "NMF":
                model = NMF(n_components=number_topics, init="random", random_state=0)
            else:
                raise KeyError(
                    'config["Values"]["Text"]["TopicExtractor"] was not specified'
                )

            model.fit(data)

            self.print_topics(model, vectorizer, number_words)

            ontology = "topic"

            words = vectorizer.get_feature_names_out()
            for topic_idx, topic in enumerate(model.components_):
                topicIdentifier = metadataFormatter.replaceForbiddenValues(
                    str(uuid.uuid4()) + "_" + str(topic_idx + 1)
                )

                values = []
                values.append(
                    {"predicate": "a", "object": "http://xmlns.com/foaf/0.1/topic"}
                )
                rootValues = []
                for word, topicRelevancy in [
                    (words[i], topic[i])
                    for i in topic.argsort()[: -number_words - 1 : -1]
                ]:
                    formattedWord = metadataFormatter.replaceForbiddenValues(word)
                    wordEntry = "{}ontologies/{}/attributes#{}".format(
                        metadataFormatter.getBaseUrl(config), ontology, formattedWord
                    )
                    values.append(
                        {
                            "subject": wordEntry,
                            "predicate": "rdf:value",
                            "object": topicRelevancy,
                        }
                    )
                    rootValues.append({"predicate": "topic:about", "object": wordEntry})

                graphOptions = {
                    "identifier": fileInfo["identifier"] + "/" + topicIdentifier,
                    "ontology": ontology,
                    "values": values,
                }
                metadata += metadataCreation.createGraphForFileGraph(
                    fileInfo, config, graphOptions
                )
                metadata += metadataCreation.addMetadataToFileGraph(
                    fileInfo,
                    config,
                    {
                        "additionalPrefixes": [
                            "@prefix topic: <{}ontologies/topic#>".format(
                                metadataFormatter.getBaseUrl(config)
                            )
                        ],
                        "values": rootValues,
                    },
                )

            if (
                "Debug" in config["Values"]
                and "VisualizeTopics" in config["Values"]["Debug"]
                and config["Values"]["Debug"]["VisualizeTopics"]
            ):
                visualisation = pyLDAvisSklearn.prepare(
                    model, data, vectorizer, mds="mmds"
                )
                if not os.path.exists("output"):
                    os.makedirs("output")
                htmlFile = (
                    "output/"
                    + fileInfo["identifier"]
                    + "."
                    + config["Values"]["Text"]["TopicExtractor"]
                    + ".html"
                )
                log.info('Storing LDAVis html to "' + htmlFile + '".')
                pyLDAvis.save_html(visualisation, htmlFile)

        return metadata, "trig"
