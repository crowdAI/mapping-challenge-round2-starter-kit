#!/bin/bash


echo "SUBMISSION : $k"

RANDOM_STRING=`echo $RANDOM | tr '[0-9]' '[a-zA-Z]'`

echo $RANDOM_STRING >> something1
git add .
git commit -am "Added random string"
git tag -am "Adding tag $RANDOM_STRING " $RANDOM_STRING
git push crowdai $RANDOM_STRING
