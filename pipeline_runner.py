import os, os.path
from os import listdir
from os.path import isfile, join
import uuid

from defaultConfigs import setDefaultLogging, getDefaultConfig

setDefaultLogging()

from MetadataExtractor.pipeline import run_pipeline

current_dir = os.path.dirname(os.path.realpath(__file__))
examples_folder = join(current_dir, "Examples")

fileInformation = [{ 'identifier': f, 'file': join(examples_folder, f), 'version': "1234" } for f in listdir(examples_folder) if isfile(join(examples_folder, f))]

config = getDefaultConfig()

if __name__ == "__main__":
    run_pipeline(fileInformation, config)
