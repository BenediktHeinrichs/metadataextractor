from .IDataExtract import IDataExtract
import pandas
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import logging

log = logging.getLogger(__name__)

# TODO: Implement with the MimeTypes here and get information from a dataframe (https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#other-file-formats)
class PandasExtract(IDataExtract):
    def extract(self, fileInfo):
        log.info('Extracting metadata with pandas "' + fileInfo["file"] + '".')
        text = ""
        metadata = ""
        # TODO: Implement
        return (text, metadata)

    def registerMimeTypes(self):
        # TODO: Implement
        self.mimeTypes["concrete"] = []
