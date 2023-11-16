import speech_recognition as sr
import wave
import contextlib
from pydub import AudioSegment
from MetadataExtractor.Util import speech_recognition_enhancer, google_cloud_long
import logging

log = logging.getLogger(__name__)
import os, os.path

from .IAudioExtract import IAudioExtract


class SpeechRecognitionExtract(IAudioExtract):
    def convert_mp3_to_wav(self, file):
        sound = AudioSegment.from_mp3(file)
        file = file.replace(".mp3", ".wav")
        sound.export(file, format="wav")
        return file

    def audio_extract(self, fileInfo):
        file = fileInfo["file"]
        config = self._IExtract__config
        log.info('Extracting audio with speech recognition from "' + file + '".')
        r = sr.Recognizer()
        mp3File = False
        if ".mp3" in file:
            file = self.convert_mp3_to_wav(file)
            mp3File = True
        text = ""
        with sr.AudioFile(file) as source:
            audio = r.record(source)
            if (
                "Values" in config
                and "Audio" in config["Values"]
                and "Google_Cloud_Credentials_File" in config["Values"]["Audio"]
                and config["Values"]["Audio"]["Google_Cloud_Credentials_File"]
                and os.path.exists(
                    config["Values"]["Audio"]["Google_Cloud_Credentials_File"]
                )
            ):
                duration = 0
                with contextlib.closing(wave.open(file, "r")) as f:
                    frames = f.getnframes()
                    rate = f.getframerate()
                    duration = frames / float(rate)
                if (
                    duration >= 60
                    and config["Values"]["Audio"]["Google_Cloud_Bucket_Name"]
                ):
                    text = google_cloud_long.google_transcribe(
                        file,
                        bucket_name=config["Values"]["Audio"][
                            "Google_Cloud_Bucket_Name"
                        ],
                        credentials_json=config["Values"]["Audio"][
                            "Google_Cloud_Credentials_File"
                        ],
                        enable_automatic_punctuation=True,
                    )
                else:
                    enhancedRecognizer = (
                        speech_recognition_enhancer.EnhancedSpeechRecognition()
                    )
                    text = enhancedRecognizer.recognize_google_cloud(
                        audio,
                        credentials_json=config["Values"]["Audio"][
                            "Google_Cloud_Credentials_File"
                        ],
                        enable_automatic_punctuation=True,
                    )

            else:
                text = r.recognize_whisper(audio, translate=True)
        if mp3File:
            os.remove(file)
        return (text, "")

    def extract(self, fileInfo):
        return self.audio_extract(fileInfo)
