import uuid
from MetadataExtractor.Util import metadataFormatter


def createGraphForFileGraph(fileInfo, config, graphOptions, dataGraphUsage=False):
    values = graphOptions["values"]

    ontology = None
    if "ontology" in graphOptions:
        ontology = graphOptions["ontology"]

    if "identifier" in graphOptions:
        identifier = graphOptions["identifier"]
    else:
        identifier = str(uuid.uuid4())
    identifier = metadataFormatter.formatIdentifier(identifier)

    additionalPrefixes = []
    if "additionalPrefixes" in graphOptions:
        additionalPrefixes = graphOptions["additionalPrefixes"]

    trig = getPrefixes(additionalPrefixes, config, ontology)

    ontologyGraphUrl = getOntologyGraphUrl(config)
    graphString = "<{}{}>".format(ontologyGraphUrl, identifier)

    trig += graphString + " {\n"

    ontologyEntryUrl = getOntologyEntryUrl(config)
    subjectString = "<{}{}>".format(ontologyEntryUrl, identifier)
    trig += addValues(subjectString, values)

    trig += "}\n"

    if "referencePredicate" in graphOptions:
        referencePredicate = graphOptions["referencePredicate"]
    else:
        referencePredicate = "dcterms:hasPart"

    trig += addMetadataToFileGraph(
        fileInfo,
        config,
        {
            "values": [
                {
                    "predicate": referencePredicate,
                    "object": getOntologyGraphUrl(config) + identifier,
                }
            ]
        },
        dataGraphUsage,
    )

    return trig


def addEntryToFileGraph(fileInfo, config, graphOptions, dataGraphUsage=False):
    values = graphOptions["values"]

    ontology = None
    if "ontology" in graphOptions:
        ontology = graphOptions["ontology"]

    if "identifier" in graphOptions:
        identifier = graphOptions["identifier"]
    else:
        identifier = str(uuid.uuid4())
    identifier = metadataFormatter.formatIdentifier(identifier)

    additionalPrefixes = []
    if "additionalPrefixes" in graphOptions:
        additionalPrefixes = graphOptions["additionalPrefixes"]

    trig = getPrefixes(additionalPrefixes, config, ontology)

    graphString = "<{}{}>".format(
        getFileGraph(config), metadataFormatter.formatIdentifier(fileInfo["identifier"])
    )

    trig += graphString + " {\n"

    ontologyEntryUrl = getOntologyEntryUrl(config)
    subjectString = "<{}{}>".format(ontologyEntryUrl, identifier)
    trig += addValues(subjectString, values)

    trig += "}\n"

    if "referencePredicate" in graphOptions:
        referencePredicate = graphOptions["referencePredicate"]
    else:
        referencePredicate = "rdf:describedby"

    trig += addMetadataToFileGraph(
        fileInfo,
        config,
        {
            "values": [
                {
                    "predicate": referencePredicate,
                    "object": getOntologyGraphUrl(config) + identifier,
                }
            ]
        },
        dataGraphUsage,
    )

    return trig


def addMetadataToFileGraph(fileInfo, config, graphOptions, dataGraphUsage=False):
    values = graphOptions["values"]

    additionalPrefixes = []
    if "additionalPrefixes" in graphOptions:
        additionalPrefixes = graphOptions["additionalPrefixes"]

    trig = getPrefixes(additionalPrefixes, config)

    identifier = metadataFormatter.formatIdentifier(fileInfo["identifier"])

    addPrefix = "@"
    if "@" in identifier:
        addPrefix = "&"

    dataGraph = addPrefix + "type=data"
    metadataGraph = addPrefix + "type=metadata"

    if "version" in fileInfo:
        dataGraph += "&version=" + fileInfo["version"]
        metadataGraph += "&version=" + fileInfo["version"]

    dataGraph += "&extracted=true"
    metadataGraph += "&extracted=true"

    identifier = identifier.replace("&type=data", "")

    trig += "<{}{}/{}>".format(
        getFileGraph(config), identifier, dataGraph if dataGraphUsage else metadataGraph
    )
    trig += " {\n"

    subjectString = "<{}{}>".format(getFileGraph(config), identifier)
    trig += addValues(subjectString, values)

    trig += "}\n"

    return trig


def getFileGraph(config):
    return metadataFormatter.getFileUrl(config)


def addValues(subjectString, values):
    trig = ""
    for value in values:
        if "subject" in value:
            valueSubjectString = metadataFormatter.subjectToRepresentation(
                value["subject"]
            )
        else:
            valueSubjectString = subjectString
        predicateString = metadataFormatter.predicateToRepresentation(
            value["predicate"]
        )
        objectString = metadataFormatter.objectToRepresentation(value["object"])
        trig += "\t{} {} {} .\n".format(
            valueSubjectString, predicateString, objectString
        )
    return trig


def getPrefixes(additionalPrefixes, config, ontology=None):
    trig = ""
    trig += "@prefix dc: <http://purl.org/dc/elements/1.1/> .\n"
    trig += "@prefix dcterms: <http://purl.org/dc/terms/> .\n"
    trig += "@prefix ns: <http://www.w3.org/ns/ma-ont#> .\n"
    trig += "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
    trig += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    trig += "@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n"

    if ontology is not None:
        trig += "@prefix {}: <{}> .\n".format(
            getOntologyGraphName(ontology), getOntologyGraphUrl(config)
        )
        trig += "@prefix {}: <{}ontologies/{}#> .\n".format(
            ontology, metadataFormatter.getBaseUrl(config), ontology
        )
        trig += "@prefix {}: <{}> .\n".format(
            getOntologyAttributes(ontology), getOntologyAttributesUrl(config, ontology)
        )
        trig += "@prefix {}: <{}> .\n".format(
            getOntologyEntry(ontology), getOntologyEntryUrl(config)
        )

    for additionalPrefix in additionalPrefixes:
        trig += "{} .\n".format(additionalPrefix)

    return trig


def getOntologyGraphName(ontology):
    return ontology + "graph"


def getOntologyGraphUrl(config):
    return getFileGraph(config)


def getOntologyAttributes(ontology):
    return ontology + "attr"


def getOntologyUrl(config, ontology):
    return "{}ontologies/{}#".format(
        metadataFormatter.getBaseUrl(config),
        ontology,
    )


def getOntologyAttributesUrl(config, ontology):
    return "{}ontologies/{}/attributes#".format(
        metadataFormatter.getBaseUrl(config),
        ontology,
    )


def getOntologyEntry(ontology):
    return ontology + "entry"


def getOntologyEntryUrl(config):
    return getFileGraph(config)
