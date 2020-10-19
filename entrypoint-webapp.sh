#!/bin/sh
sleep 60
cd ${PROJECT_DIR}/
python manage.py makemigrations blog
python manage.py migrate
gunicorn --pythonpath '${PROJECT_DIR}/' hoker_newz.wsgi:application -w 2 -b 0.0.0.0:8000