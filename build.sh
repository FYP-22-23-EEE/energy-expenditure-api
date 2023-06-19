#!/bin/bash

# Name of the Docker image
IMAGE_NAME="my-fastapi-app"

# Build the Docker image
docker build -t $IMAGE_NAME .

echo "Docker image $IMAGE_NAME has been built successfully."
