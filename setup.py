from setuptools import setup, find_packages
from distutils.util import convert_path
import os, os.path

packageName = "MetadataExtractor"

current_dir = os.path.dirname(os.path.realpath(__file__))
main_ns = {}
ver_path = "{}\\{}\\_version.py".format(current_dir, packageName)
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip("\n") for l in f if l.strip("\n") and not l.startswith("#")]


requirements = parse_requirements("{}\\requirements.txt".format(current_dir))

packages = find_packages(exclude=("tests*",), where=current_dir)

setup(
    name=packageName,
    version=main_ns["__version__"],
    namespace_packages=[packageName],
    description="Metadata Extraction",
    author="Benedikt Heinrichs",
    author_email="Heinrichs@itc.rwth-aachen.de",
    url="",
    packages=packages,
    package_dir={"MetadataExtractor": packageName},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
    ],
)
