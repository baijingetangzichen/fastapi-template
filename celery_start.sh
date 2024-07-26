#!/usr/bin/env bash

set -e

CURRENT_DIR=$(cd "$(dirname "$0")";pwd)


celery  -A app.config.celery_object:celery_app worker  -l debug -Q celery_default_queue -n fastapi-task@%h