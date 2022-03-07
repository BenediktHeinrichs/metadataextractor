import os, os.path
from os import listdir
from os.path import isfile, join

from defaultConfigs import setDefaultLogging, getDefaultConfig

setDefaultLogging()

from MetadataExtractor.pipeline import run_pipeline

current_dir = os.path.dirname(os.path.realpath(__file__))
examples_folder = current_dir + "\\Examples\\"
code_folder = current_dir + "\\MetadataExtractor\\"

mypath = ".\\Examples"
fileInfos = [{ 'identifier': f, 'file': mypath + "\\" + f } for f in listdir(mypath) if isfile(join(mypath, f))]

config = getDefaultConfig()

if __name__ == "__main__":
    run_pipeline(fileInfos, config)
