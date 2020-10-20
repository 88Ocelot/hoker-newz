#!/bin/sh
sleep 5
cd ${PROJECT_DIR}/
python manage.py makemigrations blog
python manage.py migrate
python manage.py collectstatic --noinput --clear