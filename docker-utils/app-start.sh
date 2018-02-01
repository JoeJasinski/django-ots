#!/bin/bash

echo "Starting uWSGI"
PROJECT_NAME="ots"
AUTORELOAD=${AUTORELOAD:-"1"}

source ${SITE_DIR}env/bin/activate

${SITE_DIR}env/bin/uwsgi --chdir ${SITE_DIR}proj/ \
    --module=${PROJECT_NAME}.wsgi:application \
    --master \
    --env DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings \
    --vacuum \
    --max-requests=5000 \
    --virtualenv ${SITE_DIR}env/ \
    --${CONNECT_METHOD:=socket} 0.0.0.0:8000 \
    --processes $NUM_PROCS \
    --threads $NUM_THREADS \
    --python-autoreload=$AUTORELOAD \
    --honour-stdin
#    --static-map /static=${SITE_DIR}htdocs/static/ \
#    --static-map /media=${SITE_DIR}htdocs/media/ \
