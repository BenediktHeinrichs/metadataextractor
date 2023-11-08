FROM mcr.microsoft.com/devcontainers/python:0-3.10

# Add relevant files
ADD *.py /
ADD *.sh /
ADD requirements.txt /

# Install dependencies and clean up in a single layer
RUN chmod +x installDependencies.sh && chmod +x installDependenciesCleanup.sh \
    && ./installDependencies.sh && ./installDependenciesCleanup.sh