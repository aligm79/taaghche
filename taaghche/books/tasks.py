from celery import shared_task
from .cache_center import cached_layers

@shared_task(name="delete_cache")
def delete_cache(id):
    cached_layers.delete_from_cache(id)