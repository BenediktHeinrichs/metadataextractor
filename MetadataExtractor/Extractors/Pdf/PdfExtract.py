import fitz
import os
import logging

log = logging.getLogger(__name__)

from ..Interfaces.IExtract import IExtract
from .IPdfExtract import IPdfExtract


class PdfExtract(IPdfExtract):
    def use_images(self, fileInfo):
        file = fileInfo["file"]
        log.info('Extracting images from pdf file "' + file + '".')
        doc = fitz.open(file)
        config = self._IExtract__config
        extractors = config["Extractors"]
        usedType = "Image"
        texts = [""]
        finalMetadata = ""
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                outImage = "p%s-%s.png" % (i, xref)
                if pix.n - pix.alpha < 4:  # this is GRAY or RGB
                    pix.writePNG(outImage)
                else:  # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(outImage)
                    pix1 = None
                pix = None

                for extractor in extractors[usedType]:
                    (text, metadata) = extractor.extract(
                        {"identifier": outImage, "file": outImage},
                        rootFileInfo=fileInfo,
                        frameNumber=i,
                    )
                    texts.append(text)
                    finalMetadata += "\n" + metadata
                os.remove(outImage)
        return ("\n".join(texts), finalMetadata)

    def extract(self, fileInfo):
        return self.use_images(fileInfo)
