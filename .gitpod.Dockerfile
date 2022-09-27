FROM gitpod/workspace-full

RUN sudo install-packages python3-opencv openjdk-11-jdk tesseract-ocr
RUN pip install --no-cache-dir nltk
RUN python -c "import nltk; nltk.download('punkt')"
