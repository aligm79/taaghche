import json
import requests
from django.core.cache import cache, caches
from django.http import HttpResponse
from .cache_center import cached_layers
from .tasks import delete_cache


def change_book(request, id):
    delete_cache.apply_async(args=[id])
    return HttpResponse(f"book {id} changed",  "application/json")

def get_book(request, id):
    book, cache_layer = cached_layers.search(id)
    if not book:
        book = requests.get(f"https://get.taaghche.com/v2/book/{id}")
        cached_layers.cache(book, id, cache_layer)
    return HttpResponse(book, "application/json")


def get_book2(request, id):
    book = caches['memory'].get(id)
    print("1", flush=True)
    if not book:
        book = caches['default'].get(id)
        if book:
            caches['memory'].set(id, book, 5)
            print("2", flush=True)
        else:
            book = requests.get(f"https://get.taaghche.com/v2/book/{id}")
            caches['memory'].set(id, book, 5)
            caches['default'].set(id, book, 20)
            print("3", flush=True)
    return HttpResponse(book,  "application/json")