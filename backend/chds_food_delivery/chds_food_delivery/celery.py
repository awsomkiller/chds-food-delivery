from __future__ import absolute_import, unicode_literals
from celery import Celery
import os 
from django.conf import settings
from celery.schedules import crontab
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'chds_food_delivery.settings')
django.setup()

app =Celery("chds_food_delivery",backend=os.getenv("CELERY_RESULT_BACKEND"),broker=os.getenv("CELERY_BROKER_URL"))
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup=True

#schedule tasks
app.conf.beat_schedule = {
    'every_day_8_pm' :{
        'task':'apps.restaurants.tasks.Update_ordering_status',
        # 'schedule':crontab(hour=20, minute=0)
        "schedule":crontab(minute='*/1')
    }
}