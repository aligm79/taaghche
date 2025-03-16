import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taaghche.settings')

app = Celery(
    "taaghche",
    broker="pyamqp://user:password@rabbitmq//", 
    backend=None  
)
app.conf.update(
    task_ignore_result=True  
)
app.autodiscover_tasks()