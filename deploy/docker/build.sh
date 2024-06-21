#!/usr/bin/env bash

set -e

CURRENT_DIR=$(cd "$(dirname "$0")";pwd)

cd $CURRENT_DIR/tmp

version=v0.5.2

TAG="llm-sd-api:$version"

REGISTRY=${SAIL_REGISTRY_HOST:-"172.16.210.227:11443"}/sail
REMOTE_REGISTRY=${SAIL_REGISTRY_HOST:-"mirrors.beagledata.com:8816"}/sail
# build
docker build -t $TAG .
docker tag $TAG $REGISTRY/$TAG
docker push $REGISTRY/$TAG

docker tag $TAG ${REMOTE_REGISTRY}/$TAG
docker push ${REMOTE_REGISTRY}/$TAG