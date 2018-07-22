#!/bin/bash

ARG=$1

source environ.sh
./build.sh push

nvidia-docker run -it \
  --net=host \
  -v $CROWDAI_TEST_IMAGES_PATH:/test_images \
  -v /tmp:/tmp_host \
  -e CROWDAI_IS_GRADING=True \
  -e CROWDAI_TEST_IMAGES_PATH="/test_images" \
  -e CROWDAI_PREDICTIONS_OUTPUT_PATH="/tmp_host/output.json" \
  $IMAGE_NAME \
  /home/crowdai/run.sh
