import logging
from logging.config import dictConfig

import os, os.path


def setDefaultLogging():
    log_dir = "./logs"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "console": {
                    "format": "%(message)s",
                },
                "file": {
                    "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                },
            },
            "handlers": {
                "stream": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                    "level": logging.INFO,
                },
                "debug_file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "when": "midnight",
                    "utc": True,
                    "backupCount": 7,
                    "level": logging.DEBUG,
                    "filename": "{}/debug.log".format(log_dir),
                    "formatter": "file",
                    "encoding": "utf-8",
                },
                "info_file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "when": "midnight",
                    "utc": True,
                    "backupCount": 7,
                    "level": logging.INFO,
                    "filename": "{}/info.log".format(log_dir),
                    "formatter": "file",
                    "encoding": "utf-8",
                },
            },
            "root": {
                "handlers": ["stream", "debug_file", "info_file"],
                "level": logging.DEBUG,
            },
        }
    )


def getDefaultConfig():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    google_cloud_credentials_file = current_dir + "\\google_cloud_credentials.json"

    config = {
        "Extractors": {
            "Generic": ["TikaExtract"],
            "Text": [
                #"TopicExtract",
                "PikesExtract",
                #"SummaryExtract",
            ],
            "Triples": [],
            "Data": ["Hdf5Extract"],
            "Image": [
                "DescriptiveImageExtract",
                "ObjectExtract",
                "TesseractExtract",
            ],
            "Audio": [
                #"SpeechRecognitionExtract"
            ],
            "Video": ["AudioSpeechRecognitionExtract"],
            "Pdf": ["PdfExtract"],
            "Code": ["StructureExtract"],
        },
        "Refiners": {
            "Generic": ["TikaRefine"],
            "Text": ["PikesRefine"],
            "Triples": [],
            "Data": [],
            "Image": ["ImageRefine"],
            "Audio": [
                #"SpeechRecognitionRefine"
            ],
            "Video": ["AudioSpeechRecognitionRefine"],
        },
        "Settings": {
            "MetadataCombiner": ["RDFLibCombiner"],
            "MetadataMapper": [
                #"SemanticMapper"
            ],
            "Storage": ["FileAdapter"],
        },
        "Values": {
            "Generic": {
                "MagicMimeType": False,
                "TikaPdfImageExtraction": False,
                "TikaTimeout": 180,
            },
            "Debug": {
                "VisualizeTopics": False,
            },
            "Audio": {
                "Google_Cloud_Credentials_File": google_cloud_credentials_file,
                "Google_Cloud_Bucket_Name": "metadataextractionaudios",
            },
            "Text": {
                "PikesApiPoint": os.environ.get("PIKESAPIENDPOINT", "http://pikes.westeurope.cloudapp.azure.com/text2rdf"),
                "PikesBatchSize": "50",
                "PikesMergeDefinitions": True,
                "RefinePikesAutomatically": True,
                "NumberOfTopics": "10",
                "NumberOfWords": "20",
                "TopicExtractor": "NMF",
                "Vectorizer": "Tfidf",
            },
            "Video": {
                "ImageFrequency": "300",
            },
            "Settings": {
                "StoreContent": True,
                "OutputPath": "output",
                "BaseUrl": "https://purl.org/coscine",
                "FileUrl": "https://purl.org/coscine/resources/",
                "MappingService": os.environ.get("SEMANTICMAPPERPROTOCOL", "http")
                + "://"
                + os.environ.get("SEMANTICMAPPERHOST", "127.0.0.1")
                + ":"
                + os.environ.get("SEMANTICMAPPERPORT", "36542"),
                # Assumed to be in the 'Data' folder
                "ApplicationProfiles": [
                    {"file": "hdf5AP.ttl", "format": "turtle"},
                ],
                "Vocabularies": [
                    {"file": "dcterms.ttl", "format": "turtle"},
                    {"file": "schema.ttl", "format": "turtle"},
                    {"file": "hdf5Vocab.ttl", "format": "turtle"},
                ],
            },
        },
    }

    return config
