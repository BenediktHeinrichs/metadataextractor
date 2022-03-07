# To use this library, you need to have Java 7+ installed on your system as tika-python starts up the Tika REST server in the background.
# For better results, also consider installing Tesseract: https://cwiki.apache.org/confluence/display/tika/TikaOCR
from .IGenericExtract import IGenericExtract
from tika import initVM
from tika import parser
from tika import tika
import sys
import logging

log = logging.getLogger(__name__)

from ..Interfaces.IExtract import IExtract


class TikaExtract(IGenericExtract):
    def __init__(self, config):
        IExtract.__init__(self, config)
        initVM()

    def raw_extract(
        self,
        file,
        service="all",
        serverEndpoint=tika.ServerEndpoint,
        xmlContent=False,
        headers=None,
        config_path=None,
        requestOptions={},
    ):
        return tika.parse1(
            service,
            file,
            serverEndpoint,
            headers=headers,
            config_path=config_path,
            requestOptions=requestOptions,
            responseMimeType="application/rdf+xml",
        )

    def xml_file_extract(self, file):
        return parser.from_file(file, xmlContent=True)

    def file_extract(self, file):
        log.info("Extracting generic metadata with Tika.")
        config = self._IExtract__config
        headerValue = "false"
        if (
            "Values" in config
            and "Generic" in config["Values"]
            and "TikaPdfImageExtraction" in config["Values"]["Generic"]
            and config["Values"]["Generic"]["TikaPdfImageExtraction"]
        ):
            headerValue = "true"
        timeout = 180
        if (
            "Values" in config
            and "Generic" in config["Values"]
            and "TikaTimeout" in config["Values"]["Generic"]
            and config["Values"]["Generic"]["TikaTimeout"]
        ):
            timeout = config["Values"]["Generic"]["TikaTimeout"]
        return parser.from_file(
            file,
            headers={"X-Tika-PDFextractInlineImages": headerValue},
            requestOptions={"timeout": timeout},
        )

    def extract(self, fileInfo):
        return self.file_extract(fileInfo["file"])


if __name__ == "__main__":

    from argparse import ArgumentParser

    def __parse_arguments():
        arg_parser = ArgumentParser()

        arg_parser.add_argument("--file", dest="file", required=True)

        return arg_parser, arg_parser.parse_args()

    args_parser, args = __parse_arguments()

    if len(sys.argv) == 1:
        args_parser.print_help()
        sys.exit(1)

    tikaExtract = TikaExtract({})

    print(tikaExtract.file_extract(args.file))
