apt-get update
apt-get install -y --no-install-recommends git python3-opencv default-jre tesseract-ocr build-essential default-libmysqlclient-dev pkg-config wget libmagic1 libcairo2-dev
pip install --no-cache-dir --ignore-installed -r requirements.txt
python -c "import nltk; nltk.download('punkt')"
wget -O ./tika-server.jar https://archive.apache.org/dist/tika/2.7.0/tika-server-standard-2.7.0.jar
chmod +x run.sh
