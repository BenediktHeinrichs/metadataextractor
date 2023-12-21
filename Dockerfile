# Use the slim base image
FROM python:3.10-slim

WORKDIR /home/appuser

# Add relevant files
ADD *.py ./
ADD *.sh ./
ADD requirements.txt ./
ADD Data ./Data
ADD MetadataExtractor ./MetadataExtractor

# Install dependencies and clean up in a single layer
RUN chmod +x installDependencies.sh && chmod +x installDependenciesCleanup.sh \
    && ./installDependencies.sh && ./installDependenciesCleanup.sh

# Create a new user 'appuser' and switch to it
RUN useradd --create-home appuser
RUN chown -R appuser:appuser /home/appuser

# Switch to non-root user
USER appuser

RUN chmod +x getCheckpoints.sh && ./getCheckpoints.sh

# Set the entry point
CMD ["/bin/sh", "-c", "./run.sh"]
