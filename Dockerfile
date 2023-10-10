FROM python:3.10
ADD *.py /
ADD *.sh /
ADD requirements.txt /
ADD MetadataExtractor /MetadataExtractor
RUN add-apt-repository ppa:openjdk-r/ppa && apt-get update && apt-get install -y python3-opencv openjdk-11-jdk tesseract-ocr wget
RUN pip install --no-cache-dir -r ./requirements.txt
RUN python -c "import nltk; nltk.download('punkt')"
RUN wget -O ./tika-server.jar https://dlcdn.apache.org/tika/2.7.0/tika-server-standard-2.7.0.jar
RUN chmod +x run.sh
CMD [ "/bin/sh", "-c", "./run.sh" ]
