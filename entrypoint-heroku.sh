#!/bin/sh
sleep 5
cd ${PROJECT_DIR}/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear