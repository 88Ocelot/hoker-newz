#!/bin/sh
sleep 5
cd ${PROJECT_DIR}/
python manage.py makemigrations blog
python manage.py migrate
python manage.py collectstatic --noinput --clear
gunicorn --pythonpath '${PROJECT_DIR}/' hoker_newz.wsgi:application --reload -w 2 -b  0.0.0.0:8000