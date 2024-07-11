
# Contributing to the Metadata Extractor

Thank you for considering contributing to the Metadata Extractor project! This guide will help you get started with installing the project, adding new extractors, and running the application.

## Installing — Option A

1. **Clone the repository**: First, clone the repository to your local machine using Git.

    ```bash
    git clone https://github.com/BenediktHeinrichs/MetadataExtractor.git
    ```

2. **Install dependencies**: Navigate to the cloned directory and install the necessary dependencies.

    ```bash
    cd MetadataExtractor
    pip install -r requirements.txt
    ```

    Note that you might need to install necessary things like Java. For this, see `installDependencies.sh`.

3. **Set up environment variables**: If the project requires environment variables, set them up according to the project's documentation.

## Dev Container — Option B

This repository contains a dev container definition to run the project in a complete development environment. 

Note that setting up the container takes a while since numerous dependencies have to be installed. In the future, this might be mitigated by providing a fully installed image.

You can run the dev container by using GitHub Codespaces!

## Adding an Extractor

If you want to contribute an extractor, this part should guide you on that effort:

1. **Create a new extractor**: Extractors should be placed in the `MetadataExtractor/Extractors/{Type}` directory. The `{Type}` denotes the category the to be extracted file falls under. Create a new Python file for your extractor, following the naming convention `YourExtractorNameExtract.py`.

2. **Implement extractor logic**: Your extractor should inherit from the base extractor interface and implement the required methods. Refer to the existing extractors for examples.

    ```python
    from .IImageExtract import IImageExtract

    import logging
    log = logging.getLogger(__name__)

    class YourExtractorNameExtract(IImageExtract):
        def extract(self, fileInfo):
            # Implement your extraction logic here
            return text, metadata
    ```

3. **Create metadata**: Since the goal is to extract information from data and describe it as metadata, helper methods have been created that can transform key-value pairs to metadata. For this, see the existing implementations and use these imports:

    ```python
    from MetadataExtractor.Util import metadataCreation, metadataFormatter

    # ...
    # at some point in the code, you might create the returnable metadata like so:
        values = []
        values.append({"predicate": key, "object": value})
        metadata = metadataCreation.addMetadataToFileGraph(
            fileInfo,
            self._IExtract__config,
            {
                "additionalPrefixes": [
                    "@prefix myOntology: <{}ontologies/myOntology#>".format(
                        metadataFormatter.getBaseUrl(self._IExtract__config)
                    )
                ],
                "values": values,
            },
        ),
    # ...
    ```

4. **Optional: Implement refiner logic**: Sometimes it might make sense to create a refiner implementation that takes the output text and metadata and transforms it further. This might make sense if there are multiple extractors that need the same refining logic. You can implement such a refiner in the `MetadataExtractor\Refiners` directory. Please look at the existing ones when trying to implement one yourself.

5. **Register your extractor**: Add your extractor to the list of available extractors in `defaultConfigs.py`. The extractor is dynamically loaded in `MetadataExtractor\pipeline.py` so adding it in the config is enough.

    ```python
    "Extractors": {
        # ...
        "Image": [
            # ...
            "YourExtractorNameExtract",
            # ...
        ],
        # ...
    },
    ```

## Running it

The Metadata Extractor can be run in two modes: as a server or using the pipeline runner.

### Running as a Server

1. **Start the server**: Use the following command to start the Flask server.

    ```bash
    python server.py
    ```

2. **Access the API**: The server will start on `http://localhost:36541`. Use the provided API endpoints to interact with the Metadata Extractor.

### Using the Pipeline Runner

1. **Identify your data**: Identify the data you want to perform metadata extraction on and put it into the `Examples` directory.

1. **Run the pipeline runner**: Execute the pipeline runner script.

    ```bash
    python pipeline_runner.py
    ```

2. **Check the output**: The extracted metadata will be saved in the specified output folder or printed to the console, depending on your configuration.

## Submitting a Pull Request

Once you've made your changes and tested them, you're ready to submit a pull request. Make sure your code follows the project's coding standards and include any necessary test files and documentation updates. Don't forget to update the version number in `MetadataExtractor\_version.py`.

Thank you for contributing to the Metadata Extractor!
