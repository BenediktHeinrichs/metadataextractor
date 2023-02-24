def fixMimeType(mimeType: str, extension: str): 
    if (mimeType == "audio/mp4"):
        mimeType = "video/mp4"
    if (extension == ".fcs"):
        mimeType = "application/fcs"
    return mimeType
