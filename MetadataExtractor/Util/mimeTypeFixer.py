def fixMimeType(mimeType: str, extension: str):
    if ";" in mimeType:
        mimeType = mimeType[: mimeType.index(";")]
    if mimeType == "audio/mp4":
        mimeType = "video/mp4"
    if extension == ".fcs":
        mimeType = "application/fcs"
    return mimeType
