# Use the slim base image
FROM python:3.10-slim

# Add relevant files
ADD *.py /
ADD *.sh /
ADD requirements.txt /
ADD Data /Data
ADD MetadataExtractor /MetadataExtractor

# Install dependencies and clean up in a single layer
RUN chmod +x installDependencies.sh && chmod +x installDependenciesCleanup.sh \
    && ./installDependencies.sh && ./installDependenciesCleanup.sh

# Set the entry point
CMD ["/bin/sh", "-c", "./run.sh"]
