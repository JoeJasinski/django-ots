#!/bin/bash

export SITE_DIR=${SITE_DIR:-"/site/"}
export PYTHONPATH="${SITE_DIR}proj/:${PYTHONPATH}"

cd ${SITE_DIR}proj/
source ${SITE_DIR}/env/bin/activate

if [ "$1" == 'init' ]; then
    echo "Run Migrations"
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py migrate
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py collectstatic
elif [ "$1" == 'manage' ]; then
    shift
    echo "Manage.py $@"
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py $@
else
    exec "$@"
fi
