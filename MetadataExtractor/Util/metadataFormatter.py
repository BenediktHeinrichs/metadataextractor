import validators
import urllib.parse

defaultBaseUrl = "https://purl.org/metadataExtractor"


def getBaseUrl(config):
    if (
        "Values" in config
        or "Settings" in config["Values"]
        or "BaseUrl" in config["Values"]["Settings"]
    ):
        return config["Values"]["Settings"]["BaseUrl"]
    return defaultBaseUrl


def getFileUrl(config):
    if (
        "Values" in config
        or "Settings" in config["Values"]
        or "FileUrl" in config["Values"]["Settings"]
    ):
        if "HandlePrefix" in config["Values"]["Settings"]:
            return config["Values"]["Settings"]["FileUrl"].replace(
                "{HandlePrefix}", config["Values"]["Settings"]["HandlePrefix"]
            )
        return config["Values"]["Settings"]["FileUrl"]
    return defaultBaseUrl


def replaceForbiddenValues(startString: str):
    endString = startString.replace(" ", "_")
    endString = endString.replace("-", "_")
    endString = endString.replace("–", "_")
    endString = endString.replace("/", "_")
    endString = endString.replace("'", "_")
    endString = endString.replace(".", "_")
    endString = endString.replace(",", "_")
    endString = endString.replace("&", "_")
    endString = endString.replace("(", "")
    endString = endString.replace(")", "")
    endString = endString.replace("[", "")
    endString = endString.replace("]", "")
    endString = endString.replace(":", "_")
    return endString


def subjectToRepresentation(subject):
    return predicateToRepresentation(subject)


def predicateToRepresentation(predicate):
    if validators.url(predicate):
        return urlRepresentation(predicate)
    return predicate


def objectToRepresentation(obj):
    objType = type(obj)
    if objType == str and validators.url(obj):
        return urlRepresentation(obj)
    elif objType == str:
        return stringRepresentation(obj)
    elif objType == bytes:
        return stringRepresentation(obj.decode("utf-8"))
    elif objType == list:
        return ", ".join([objectToRepresentation(entry) for entry in obj])
    return stringRepresentation(str(obj))


def stringRepresentation(obj: str):
    seperateCharacter = '"'
    if "\n" in obj:
        seperateCharacter = '"""'
    return "{}{}{}".format(
        seperateCharacter, structureValueRefactorer(obj), seperateCharacter
    )


def urlRepresentation(obj: str):
    return "<{}>".format(obj)


def structureValueRefactorer(startString: str):
    endString = startString.replace("\n", " ")
    endString = endString.replace("\r", " ")
    endString = endString.replace("\\", "/")
    endString = endString.replace('"', "'")
    return endString


def formatIdentifier(file: str):
    formatted_file = urllib.parse.quote_plus(file, safe="/@&=")
    return formatted_file.replace(".", "_")
