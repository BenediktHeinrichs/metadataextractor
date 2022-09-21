def fixMimeType(mimeType: str): 
    if (mimeType == "audio/mp4"):
        mimeType = "video/mp4"
    return mimeType