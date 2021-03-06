import os
from datetime import timedelta

import django

if os.environ.get("ENV", "LOCAL") == "LOCAL":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hoker_newz.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hoker_newz.settings.prod")
django.setup()
from celery import Celery
from django.utils import timezone

from upvotes.models import Upvote

app = Celery("hoker_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def reset_upvotes_daily():
    Upvote.objects.filter(upvoted_at__lte=timezone.now() - timedelta(hours=24)).delete()
