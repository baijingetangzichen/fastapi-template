#!/usr/bin/env bash

set -e

CURRENT_DIR=$(cd "$(dirname "$0")";pwd)

cd ${CURRENT_DIR}/app

export PROJECT_SERVER_PORT=${PROJECT_SERVER_PORT:-"32359"}
export WORKERS_NUM=${WORKERS_NUM:-2}
export LOG_LEVEL=${LOG_LEVEL:-"debug"}
LOG_LEVEL=$(echo ${LOG_LEVEL} | tr A-Z a-z)

if [ "$#" -lt 1 ]; then
  uvicorn fastapi_template:app --host 0.0.0.0 --port ${PROJECT_SERVER_PORT} --log-level=$LOG_LEVEL --workers ${WORKERS_NUM} --log-config uvicorn_log_config.json
elif [ $1 = "t" ]; then
  gunicorn -c gunicorn.conf.py fastapi_template:app --log-config-json gunicorn_log_config.json
fi
