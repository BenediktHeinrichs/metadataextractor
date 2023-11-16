import moviepy.editor as mp
from .IVideoExtract import IVideoExtract
import os
import logging
import cv2
import uuid

log = logging.getLogger(__name__)


class AudioSpeechRecognitionExtract(IVideoExtract):
    def __levenshtein(self, s1, s2):
        if len(s1) < len(s2):
            return self.__levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = (
                    previous_row[j + 1] + 1
                )  # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1  # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def __metadataCompare(self, s1, s2):
        # TODO: implement correctly
        return self.__levenshtein(s1, s2)

    def use_audio(self, fileInfo):
        config = self._IExtract__config
        clip = mp.VideoFileClip(fileInfo["file"])
        audioFileName = os.path.basename(fileInfo["identifier"]) + ".wav"
        extractors = config["Extractors"]
        usedType = "Audio"
        text = ""
        metadata = ""
        if clip.audio is not None:
            clip.audio.write_audiofile(audioFileName)
            for extractor in extractors[usedType]:
                (extractedText, extractedMetadata) = extractor.extract(
                    {"identifier": fileInfo["identifier"], "file": audioFileName}
                )
                text += extractedText
                metadata += extractedMetadata
            os.remove(audioFileName)
        return (text, metadata)

    def use_images(self, fileInfo):
        config = self._IExtract__config
        cap = cv2.VideoCapture(fileInfo["file"])
        count = 0
        extractors = config["Extractors"]
        usedType = "Image"
        success = True
        texts = [""]
        finalMetadata = ""
        lastTexts = {}
        lastMetadata = {}
        while success:
            success, image = cap.read()
            if count % int(config["Values"]["Video"]["ImageFrequency"]) == 1:
                print("Extracting information from frame " + str(count))
                imageFileIdentifier = str(uuid.uuid4())
                imageFileName = imageFileIdentifier + "_" + str(count) + ".jpg"
                cv2.imwrite(imageFileName, image)
                for extractor in extractors[usedType]:
                    (text, metadata) = extractor.extract(
                        {"identifier": imageFileIdentifier, "file": imageFileName},
                        rootFileInfo=fileInfo,
                        frameNumber=count,
                    )
                    if (
                        self.__levenshtein(
                            text, lastTexts[extractor] if extractor in lastTexts else ""
                        )
                        > 3
                        or self.__metadataCompare(
                            metadata,
                            lastMetadata[extractor]
                            if extractor in lastMetadata
                            else "",
                        )
                        > 2
                    ):
                        texts.append(text)
                        finalMetadata += "\n" + metadata
                        lastTexts[extractor] = text
                        lastMetadata[extractor] = metadata
                os.remove(imageFileName)
            count += 1
        return ("\n".join(texts), finalMetadata)

    def video_extract(self, fileInfo):
        log.info('Extracting text from video "' + fileInfo["file"] + '".')
        (imageText, imageMetadata) = self.use_images(fileInfo)
        (audioText, audioMetadata) = self.use_audio(fileInfo)
        return (imageText + "\n" + audioText, imageMetadata + "\n" + audioMetadata)

    def extract(self, fileInfo):
        return self.video_extract(fileInfo)
