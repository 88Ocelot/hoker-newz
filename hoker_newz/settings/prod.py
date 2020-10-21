from hoker_newz.settings.base import *
import django_heroku
import os

ALLOWED_HOSTS = ("https://hoker-newz.herokuapp.com/",)
django_heroku.settings(locals())
CELERY_BROKER_URL = os.environ.get("REDIS_URL")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL")
DEBUG = False
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
STATIC_ROOT = os.path.join(os.path.dirname( __file__ ), '..', 'static')
STATIC_URL = "/static/"
