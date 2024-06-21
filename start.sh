#!/usr/bin/env bash

set -e

CURRENT_DIR=$(cd "$(dirname "$0")";pwd)

cd /llm-sd-api/api

export PROJECT_SERVER_PORT=${PROJECT_SERVER_PORT:-"32346"}
export WORKERS_NUM=${WORKERS_NUM:-1}
export LOG_LEVEL=${LOG_LEVEL:-"debug"}
LOG_LEVEL=$(echo ${LOG_LEVEL} | tr A-Z a-z)

uvicorn main:app --host 0.0.0.0 --port ${PROJECT_SERVER_PORT} --log-level=$LOG_LEVEL --workers ${WORKERS_NUM}
