#!/usr/bin/env bash

CURRENT_DIR=$(cd "$(dirname "$0")";pwd)
PROJECT_DIR=$(cd "$(dirname "$0")/../../";pwd)
echo 项目路径 ${PROJECT_DIR}
if [ -d ${CURRENT_DIR}/tmp ];then
  rm -fr ${CURRENT_DIR}/tmp
  mkdir -p ${CURRENT_DIR}/tmp
else
  mkdir -p ${CURRENT_DIR}/tmp
fi

cp -r ${PROJECT_DIR}/api ${CURRENT_DIR}/tmp
cp -r ${PROJECT_DIR}/static ${CURRENT_DIR}/tmp
cp -r ${CURRENT_DIR}/Dockerfile ${CURRENT_DIR}/tmp

cp -r ${PROJECT_DIR}/requirements.txt ${CURRENT_DIR}/tmp
cp -r ${PROJECT_DIR}/start.sh ${CURRENT_DIR}/tmp