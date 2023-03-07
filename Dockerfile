FROM python:3.10
ADD *.py /
ADD *.sh /
ADD requirements.txt /
ADD MetadataExtractor /MetadataExtractor
RUN apt-get update && apt-get install -y python3-opencv openjdk-11-jdk tesseract-ocr wget
RUN pip install --no-cache-dir -r ./requirements.txt
RUN python -c "import nltk; nltk.download('punkt')"
CMD [ "/bin/bash", "-c", "./run.sh" ]
