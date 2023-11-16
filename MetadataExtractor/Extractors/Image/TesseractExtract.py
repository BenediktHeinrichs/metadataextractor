import pytesseract as tess
from PIL import Image
import logging
from .IImageExtract import IImageExtract

log = logging.getLogger(__name__)


# Follow installation here: https://pypi.org/project/pytesseract/
class TesseractExtract(IImageExtract):
    def image_extract(self, fileInfo):
        file = fileInfo["file"]
        log.info('Extracting text with Tesseract from image "' + file + '".')
        try:
            img = Image.open(file)
            text = tess.image_to_string(img)
            img.close()
        except Exception:
            return ("", "")
        return (text, "")

    # TODO: Think of something to deal with rootFile and frameNumber for images
    def extract(self, fileInfo, rootFileInfo=None, frameNumber=None):
        return self.image_extract(fileInfo)
