# Use the slim base image
FROM python:3.10-slim

# Add relevant files
ADD *.py /
ADD *.sh /
ADD requirements.txt /
ADD MetadataExtractor /MetadataExtractor

# Install dependencies and clean up in a single layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    git python3-opencv default-jre tesseract-ocr build-essential default-libmysqlclient-dev pkg-config wget libmagic1 \
    && pip install --no-cache-dir -r requirements.txt \
    && python -c "import nltk; nltk.download('punkt')" \
    && wget -O ./tika-server.jar https://archive.apache.org/dist/tika/2.7.0/tika-server-standard-2.7.0.jar \
    && chmod +x run.sh \
    && apt-get remove -y --auto-remove git build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the entry point
CMD ["/bin/sh", "-c", "./run.sh"]
