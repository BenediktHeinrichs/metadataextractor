from speech_recognition import (
    AudioData,
    Recognizer,
    RequestError,
    URLError,
)
import os


class EnhancedSpeechRecognition(Recognizer):
    def recognize_google_cloud(
        self,
        audio_data,
        credentials_json=None,
        language="en-US",
        preferred_phrases=None,
        show_all=False,
        enable_automatic_punctuation=False,
    ):
        """
        Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Cloud Speech API.
        This function requires a Google Cloud Platform account; see the `Google Cloud Speech API Quickstart <https://cloud.google.com/speech/docs/getting-started>`__ for details and instructions. Basically, create a project, enable billing for the project, enable the Google Cloud Speech API for the project, and set up Service Account Key credentials for the project. The result is a JSON file containing the API credentials. The text content of this JSON file is specified by ``credentials_json``. If not specified, the library will try to automatically `find the default API credentials JSON file <https://developers.google.com/identity/protocols/application-default-credentials>`__.
        The recognition language is determined by ``language``, which is a BCP-47 language tag like ``"en-US"`` (US English). A list of supported language tags can be found in the `Google Cloud Speech API documentation <https://cloud.google.com/speech/docs/languages>`__.
        If ``preferred_phrases`` is an iterable of phrase strings, those given phrases will be more likely to be recognized over similar-sounding alternatives. This is useful for things like keyword/command recognition or adding new phrases that aren't in Google's vocabulary. Note that the API imposes certain `restrictions on the list of phrase strings <https://cloud.google.com/speech/limits#content>`__.
        Returns the most likely transcription if ``show_all`` is False (the default). Otherwise, returns the raw API response as a JSON dictionary.
        Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if the speech recognition operation failed, if the credentials aren't valid, or if there is no Internet connection.
        """
        assert isinstance(audio_data, AudioData), "``audio_data`` must be audio data"
        if credentials_json is None:
            assert os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is not None
        assert isinstance(language, str), "``language`` must be a string"
        assert preferred_phrases is None or all(
            isinstance(preferred_phrases, (type(""), type("")))
            for preferred_phrases in preferred_phrases
        ), "``preferred_phrases`` must be a list of strings"

        try:
            import socket
            from google.cloud import speech
            from google.cloud.speech import enums
            from google.cloud.speech import types
            from google.api_core.exceptions import GoogleAPICallError
        except ImportError:
            raise RequestError(
                "missing google-cloud-speech module: ensure that google-cloud-speech is set up correctly."
            )

        if credentials_json is not None:
            client = speech.SpeechClient.from_service_account_json(credentials_json)
        else:
            client = speech.SpeechClient()

        flac_data = audio_data.get_flac_data(
            convert_rate=None
            if 8000 <= audio_data.sample_rate <= 48000
            else max(
                8000, min(audio_data.sample_rate, 48000)
            ),  # audio sample rate must be between 8 kHz and 48 kHz inclusive - clamp sample rate into this range
            convert_width=2,  # audio samples must be 16-bit
        )
        audio = types.RecognitionAudio(content=flac_data)

        config = {
            "encoding": enums.RecognitionConfig.AudioEncoding.FLAC,
            "sample_rate_hertz": audio_data.sample_rate,
            "language_code": language,
        }
        if preferred_phrases is not None:
            config["speechContexts"] = [types.SpeechContext(phrases=preferred_phrases)]
        if show_all:
            config[
                "enableWordTimeOffsets"
            ] = True  # some useful extra options for when we want all the output
        # new google cloud speech to text feature: https://cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig
        if enable_automatic_punctuation:
            config["enable_automatic_punctuation"] = True
        opts = {}
        if self.operation_timeout and socket.getdefaulttimeout() is None:
            opts["timeout"] = self.operation_timeout

        config = types.RecognitionConfig(**config)

        try:
            response = client.recognize(config, audio, **opts)
        except GoogleAPICallError as e:
            raise RequestError(e)
        except URLError as e:
            raise RequestError("recognition connection failed: {0}".format(e.reason))

        if show_all:
            return response
        if len(response.results) == 0:
            return ""

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript.strip() + " "
        return transcript
