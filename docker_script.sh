#! /usr/bin/env bash

TIMESTAMP=$(date +"%Y%m%d%H%M%S")
HELLOAPP="ampregistry:5000/hello_app:$TIMESTAMP"
RED='\033[0;31m'
NC='\033[0m' # No Color

docker build -f ./Dockerfile -t $HELLOAPP .
docker push $HELLOAPP
echo -e "$RED$HELLOAPP$NC"