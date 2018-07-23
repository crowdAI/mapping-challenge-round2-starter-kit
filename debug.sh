#!/bin/bash

source environ.sh
./build.sh

# If the output file already exists, delete it
if [ -e "/tmp/output.json" ]; then
    rm -rf /tmp/output.json
fi 

# Run the build docker container
# - Mount the test images from the host to /test_images inside the container
# - Assign the correct environment variables
nvidia-docker run -it \
  --net=host \
  -v $CROWDAI_TEST_IMAGES_PATH:/test_images \
  -v /tmp:/tmp_host \
  -e CROWDAI_TEST_IMAGES_PATH="/test_images" \
  -e CROWDAI_PREDICTIONS_OUTPUT_PATH="/tmp_host/output.json" \
  $IMAGE_NAME \
  /home/crowdai/run.sh

echo "Final Predictions at /tmp/output.json"
echo "Filesize (bytes) of output : `cat /tmp/output.json | wc -c `"
