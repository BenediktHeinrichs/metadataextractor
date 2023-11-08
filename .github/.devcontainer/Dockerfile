FROM mcr.microsoft.com/devcontainers/python:0-3.10

WORKDIR ../../

# Add relevant files
ADD *.py /
ADD *.sh /
ADD requirements.txt /
ADD Data /Data
ADD MetadataExtractor /MetadataExtractor

# Install dependencies and clean up in a single layer
RUN chmod +x installDependencies.sh && chmod +x installDependenciesCleanup.sh \
    && ./installDependencies.sh && ./installDependenciesCleanup.sh
