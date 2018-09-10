# mapping-challenge-starter-kit (Round-2)
![CrowdAI-Logo](https://github.com/crowdAI/crowdai/raw/master/app/assets/images/misc/crowdai-logo-smile.svg?sanitize=true)

[![gitter-badge](https://badges.gitter.im/crowdAI/crowdai-mapping-challenge.png)](https://gitter.im/crowdAI/crowdai-mapping-challenge)

This is a set of instructions to make a submission to the **Round 2** of [crowdAI Mapping Challenge](https://www.crowdai.org/challenges/mapping-challenge).   
In Round 2, Participants are required to submit their code as repositories with [Dockerfiles](https://docs.docker.com/engine/reference/builder/), so that we can build and execute their code as containers. The submitted code will be used to make predictions for an arbitrary number of test images to evaluate its performance. 

The code can be added as **private repository** on [gitlab.crowdai.org](https://gitlab.crowdai.org). And each **tag push** to the repository will be considered as a submission. After every tag push, please refer to the "Issues" section of your repository for the evaluation logs related to your submission. You can find more details about the submission process in the following sections.

The submitted code will be used to build a docker image (as described in [build.sh](build.sh)), which will be orchestrated by our evaluation interface (similar to) as described in [debug.sh](debug.sh). Your code is supposed to accept the path to a folder of images, and write the predicted annotations to a specified file path. 
**Note** : Your code is expected to only do the inference (and not the training).

# Contents
* [Prerequisites](#prerequisites-dependencies)
* [Setup](#setup)
* [Build Image Locally](#build-image-locally)
* [Debug Locally](#debug-locally)
* [Changes to your Code](#changes-to-your-code)
* [Important Concepts](#important-concepts)
  - [Repository Structure](#repository-structure)
    - crowdai.json
    - Dockerfile
  - [Submission](#submission)
* [Hardware Limits](#hardware-limits)
* [Submission TL;DR](#submission-tldr)

# Prerequisites Dependencies
* **docker-ce**: Install instructions [here](https://docs.docker.com/install/)
* **nvidia-docker**: Install instructions [here](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0))

# Setup
```
# Clone Repository
git clone git@github.com:crowdAI/mapping-challenge-round2-starter-kit.git
cd mapping-challenge-round2-starter-kit
cp environ.sh.example environ.sh
# Edit `environ.sh` to point to your local test_images directory
source environ.sh
```

# Build Image Locally
```
cd mapping-challenge-round2-starter-kit
source environ.sh
./build.sh
```

# Debug Locally 
```
cd mapping-challenge-round2-starter-kit
# Remember to edit `environ.sh` to point to your local test_images directory
source environ.sh
./debug.sh
# This should write the final predictions to /tmp/output.json
```
## Changes-to-your-code
The entry point for your code in your container has to be : `/home/crowdai/run.sh`, 
and you will have access to two Environment Variables :   
* `CROWDAI_TEST_IMAGES_PATH` : Which holds the path of the folder containing all the test images
* ` CROWDAI_PREDICTIONS_OUTPUT_PATH` : Path where you are supposed to write your final predictions output (as a JSON). The predictions have to be a list of annotations, the same as what was used in Round 1. An example structure can be found [here](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Submission-Format)

* The submitted container, needs to communicate with the rest of the evaluation interface by 
using a simple api, that is abstracted by `crowdai_helpers.py`. Please do not make any changes to 
the communication protocol. [run.py](run.py) has a simple example implementation of a random submission.

# Important Concepts

## Repository Structure
* `crowdai.json`
  Each repository should have a `crowdai.json` with the following content : 
```json
{
  "challenge_id" : "crowdAIMappingChallenge",
  "grader_id" : "crowdAIMappingChallenge",
  "authors" : ["your-crowdai-username"],
  "description" : "sample description",
  "license" : "MIT",
  "gpu":false
}
```
This is used to map your submission to the said challenge.

Please specify if your code will a GPU or not for the evaluation of your model. If you specify `true` for the GPU, a **NVIDIA Titan-X (Maxwell Series) GPU** will be provided and used for the evaluation.

* `Dockerfile`
Each repository should have a valid Dockerfile which should build an image for your code.
The evaluator starts the container from your image by running the entrypoint : 
```
/home/crowdai/run.sh
```
Please refer to the [sample Dockerfile in this repository](Dockerfile) for an example on how to 
create the correct directory structure inside your image.

* The submitted container, needs to communicate with the rest of the evaluation interface by 
using a simple api, that is abstracted by `crowdai_helpers.py`. Please do not make any changes to 
the communication protocol. [run.py](run.py) has a simple example implementation of a random submission.


# Submission 
To make a submission, you will have to create a private repository on [https://gitlab.crowdai.org](https://gitlab.crowdai.org).

You will have to add your SSH Keys to your GitLab account by following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).
If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/ssh/README.html#generating-a-new-ssh-key-pair).

Then you can create a submission by making a *tag push* to your repository on [https://gitlab.crowdai.org](https://gitlab.crowdai.org). **Any tag push to your private repository is considered as a submission**
Then you can add the correct git remote by doing : 

```
cd mapping-challenge-round2-starter-kit
# Add crowdAI git remote endpoint
git remote add crowdai git@gitlab.crowdai.org:<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round2-starter-kit.git
git push crowdai master
# Update Author
sed -i 's/spMohanty/<YOUR_CROWDAI_USER_NAME>/g' crowdai.json
git commit -am "update crowdai.json"

# Create a tag for your submission and push
git tag -am "v0.1" v0.1
git push crowdai v0.1
```
You now should be able to see the details of your submission at : 
[gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round-2/issues](gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round-2/issues)

**NOTE**: Remember to update your username in the link above :wink:

**Best of Luck** 

# Hardware-Limits
Your code will be allowed to use a maximum of : 
* 1 cpu core
* upto 8GB of Memory
* upto 10GB of Disk Space
* (optional) 1 NVIDIA Titan X (Maxwell Series) GPU

**Note** Your evaluation will have a total timeout of 5 hours.

# Submission TL;DR
**Note**: This section assumes, that you have setup your SSH keys on [https://gitlab.crowdai.org](https://gitlab.crowdai.org) by following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).
```
# Clone Repository 
git clone git@github.com:crowdAI/mapping-challenge-round2-starter-kit.git
cd mapping-challenge-round2-starter-kit

# Add crowdAI git remote endpoint
git remote add crowdai git@gitlab.crowdai.org:<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round2-starter-kit.git
git push crowdai master

# Update Author
sed -i 's/spMohanty/<YOUR_CROWDAI_USER_NAME>/g' crowdai.json
git commit -am "Update crowdai.json"

# Create a tag for your submission and push
git tag -am "version 0.1" v0.1
git push crowdai v0.1
echo "Check the status of your submission at : 'https://gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round2-starter-kit/issues"
```

# Author
Sharada Mohanty <sharada.mohanty@epfl.ch>
