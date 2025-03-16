from django.urls import path
from .views import get_book, change_book

urlpatterns = [
    path("get/book/<int:id>/", get_book, name="get_book"),
    path("change/book/<int:id>/", change_book, name="change_book")
]