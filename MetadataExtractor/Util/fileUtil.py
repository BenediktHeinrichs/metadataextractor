import textract


def file_extract(file):
    return textract.process(file).decode("utf-8")
