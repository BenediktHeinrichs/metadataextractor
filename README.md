# MetadataExtractor

MetadataExtractor is a web service built on Flask for extracting metadata as [RDF](https://www.w3.org/RDF/) triples from various file types. This service utilizes a REST API for receiving files and returning metadata in multiple formats.

## Requirements

- Python 3.10+
- Additional dependencies are listed in the `installDependencies.sh` file.
  - [Apache Tika](https://tika.apache.org/)
  - [Tesseract](https://github.com/tesseract-ocr/tesseract)
  - [OpenCV](https://opencv.org/)
  - [YOLO-NAS](https://github.com/Deci-AI/super-gradients/blob/master/YOLONAS.md)
- Additional requirements are listed in the `requirements.txt` file.

## Installation

To install MetadataExtractor, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository/MetadataExtractor.git
    cd MetadataExtractor
    ```

2. Run the `installDependencies.sh` script to install required dependencies & Python packages (Linux):
    ```bash
    ./installDependencies.sh
    ```

3. If you have Docker installed, you can build and run the service using the provided `Dockerfile`.

## Running the Service

To start the service:

1. Using Python directly:
    ```bash
    python server.py
    ```

2. Using Docker:
    - Build the Docker image:
        ```bash
        docker build -t metadataextractor .
        ```
    - Run the Docker container:
        ```bash
        docker run -p 36541:36541 metadataextractor
        ```

## Configuration

- The service can be configured using the `defaultConfigs.py` module.
  - This configuration can be overwritten at every metadata extraction request
- Logging is set up via the `setDefaultLogging()` function.
- Environmental variables such as `MAX_CONTENT_LENGTH`, `METADATA_EXTRACTOR_HOST`, and `METADATA_EXTRACTOR_PORT` can be adjusted as needed.

## Version

Current API version is defined by the `__version__` attribute within the `MetadataExtractor` module.

## Usage

The service exposes several endpoints:

### POST /

- This endpoint accepts form-data with a download url or a file along with optional parameters:
  - `identifier`: A unique identifier for the file.
  - `config`: Configuration object for extraction settings.
  - `creation_date`: File's creation date.
  - `modification_date`: File's modification date.
  - `url`: Download URL of the file.
  - `file`: The file to be processed.
- Returns extracted metadata in the requested format. (JSON, Turtle, RDF/XML, JSON-LD, TriG)

### GET /defaultConfig

- Returns the default configuration JSON object for the Metadata Extractor.

### GET /version

- Returns the current version of the Metadata Extractor.

## API Response Models

The server uses defined response models to structure the JSON response. This includes the `MetadataOutput` model for the main endpoint and the `Version` model for the version endpoint.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Linting & Fixing

```
pip install ruff
ruff --fix .
ruff format .
```

### Development

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/BenediktHeinrichs/metadataextractor)
