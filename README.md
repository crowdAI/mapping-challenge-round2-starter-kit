# mapping-challenge-starter-kit (Round-2)
![CrowdAI-Logo](https://github.com/crowdAI/crowdai/raw/master/app/assets/images/misc/crowdai-logo-smile.svg?sanitize=true)

[![gitter-badge](https://badges.gitter.im/crowdAI/crowdai-mapping-challenge.png)](https://gitter.im/crowdAI/crowdai-mapping-challenge)

This is a set of instructions to make a submission to the **Round 2** of [crowdAI Mapping Challenge](https://www.crowdai.org/challenges/mapping-challenge).   
In Round 2, Participants are required to submit their code as repositories with [Dockerfiles](https://docs.docker.com/engine/reference/builder/), so that we can build and execute their code as containers. The submitted code will be used to make predictions for an arbitrary number of test images to evaluate its performance. 

The code can be added as **private repository** on [gitlab.crowdai.org](https://gitlab.crowdai.org). And each **tag push** to the repository will be considered as a submission. After every tag push, please refer to the "Issues" section of your repository for the evaluation logs related to your submission. You can find more details about the submission process in the following sections.


# Contents
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Build Image Locally](#build-image-locally)
* [Debug Locally](#debug-locally)
* [Important Concepts](#important-concepts)
  - [Repository Structure](#repository-structure)
    - crowdai.json
    - Dockerfile
  - [Submission](#submission)
* [Submission TL;DR](#submission-tl-dr)

# Prerequisites
* [docker-ce](https://docs.docker.com/install/)
* [nvidia-docker](https://github.com/NVIDIA/nvidia-docker#quickstart)

# Setup
```
git clone git@github.com:crowdAI/mapping-challenge-round2-starter-kit.git
cd mapping-challenge-round2-starter-kit
cp environ.sh.example environ.sh
# Edit `environ.sh` to point to your local test_images directory
source environ.sh
```

# Build-Image-Locally
```
cd mapping-challenge-round2-starter-kit
source environ.sh
./build.sh
```

# Debug-Locally 
```
cd mapping-challenge-round2-starter-kit
# Remember to edit `environ.sh` to point to your local test_images directory
source environ.sh
./debug.sh
# This should write the final predictions to /tmp/output.json
```

# Important-Concepts

## Repository-Structure
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
This is used to map your submission to the said challenge. And to specify if your code will need a GPU or not.
You will be provided with a NVIDIA Titan-X (Maxwell Series) GPU.

* `Dockerfile`
Each repository should have a valid Dockerfile which should build an image for your code.
The evalutor starts the container from your image by running the entrypoint : 
```
/home/crowdai/run.sh
```
Please refer to the [sample Dockerfile in this repository](Dockerfile) for an example on how to 
create the correct directory structure inside your image.

* The submitted container, needs to communicate with the rest of the evaluation interface by 
using a simple api, that is abstracted by `crowdai_helpers.py`. Please do not make any changes to 
the communication protocol. [run.py](run.py) has a simple example implementation of a random submission.


# Submission 
To make a submission, you will have to create a private repository on [https://gitlab.crowdai.org](https://gitlab.crowdai.org). And you will have to add your SSH Keys to your account by 
following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).   

Then you can create a submission by making a *tag push* to your repository on [https://gitlab.crowdai.org](https://gitlab.crowdai.org).
Then you can add the correct git remote by doing : 

```
cd mapping-challenge-round2-starter-kit
git remote add crowdai git@gitlab.crowdai.org:<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round2-starter-kit.git
git push crowdai master
sed -i 's/spMohanty/<YOUR_CROWDAI_USER_NAME>/g' crowdai.json
git commit -am "update crowdai.json"

# Create a tag for your submission
git tag -am "v0.1" v0.1
git push crowdai v0.1
```
And now you should be able to see the details of your submission at : 
[gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round-2/issues](gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round-2/issues)

**NOTE**: Remember to update your username in the link above :wink:

**Best of Luck** 

# Submission-TL-DR
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

# Create and push submission
git tag -am "version 0.1" v0.1
git push crowdai v0.1
echo "Check the status of your submission at : 'https://gitlab.crowdai.org/<YOUR_CROWDAI_USER_NAME>/mapping-challenge-round2-starter-kit/issues"
```

# Author
Sharada Mohanty <sharada.mohanty@epfl.ch>
