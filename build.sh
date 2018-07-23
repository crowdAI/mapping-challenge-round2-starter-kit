#!/bin/bash

ARGS=$1

docker build -t ${IMAGE_NAME} .

if [ "$ARGS" = "push" ]; then
  docker push ${IMAGE_NAME}
fi
