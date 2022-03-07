# MetadataExtractor

This repository provides the source code to the MetadataExtractor project and help for setting it up.

## Running Tika

1) Download the server .jar from here: [Tika Downloadsite](https://tika.apache.org/download.html)
2) Execute the tika server with `java -jar {tika-server-jar}`

## For installing the dependencies

```bash
pip install imageio==2.4.1
```

Execute in Python:

```python
import imageio
imageio.plugins.ffmpeg.download()
```

After that execute:

```bash
pip install setuptools
pip install invoke

invoke install
```

If this doesn't work, execute:

```bash
pip install -r requirements.txt
```

If you plan on using it on .mp3 files you need to install [ffmpeg](https://ffmpeg.zeranoe.com/builds/) and make it available on PATH.

## Server

For running MetadataExtractor as a server, just execute the `server.py` with Python.

Set the environment variable `METADATAEXTRACTORPORT` if you want to specify the port.

### Endpoints

There is are three endpoints present:

#### Default (/) POST

The main operation from which the Metadata Extraction can be triggered.

It expects 1-n files to be present from a multi-form upload. `enctype="multipart/form-data"` should be present.

Furthermore, it reads the data form where values like identifiers for these files ["identifier"] and a configuration extension ["config"] can be put.

#### Default Config (/defaultConfig) GET

Retrieves the default configuration currently present on the Metadata Extraction instance.

#### Version (/version) GET

Retrieves the current version of the Metadata Extraction instance.
