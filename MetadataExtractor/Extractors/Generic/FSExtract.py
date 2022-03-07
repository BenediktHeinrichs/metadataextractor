from argparse import ArgumentParser
import sys

from ..Interfaces.IExtract import IExtract
from .IGenericExtract import IGenericExtract


class FSExtract(IGenericExtract):
    def file_extract(self, file):
        # TODO: Implement FSExtract
        # https://fscrawler.readthedocs.io/en/latest/admin/fs/rest.html#simulate-upload
        raise NotImplementedError()
        # return parser.from_file(file)

    def extract(self, fileInfo):
        return self.file_extract(fileInfo["file"])


if __name__ == "__main__":

    def __parse_arguments():
        arg_parser = ArgumentParser()

        arg_parser.add_argument("--file", dest="file", required=True)

        return arg_parser, arg_parser.parse_args()

    args_parser, args = __parse_arguments()

    if len(sys.argv) == 1:
        args_parser.print_help()
        sys.exit(1)

    fsExtract = FSExtract({})

    print(fsExtract.file_extract(args.file))
