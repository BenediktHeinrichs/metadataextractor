from ..Interfaces.IRefine import IRefine


class AudioSpeechRecognitionRefine(IRefine):
    def refine_metadata(self, metadata, fileInfo, metadataformat="trig"):
        return (metadata, metadataformat)
