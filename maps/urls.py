from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/save_place/", views.save_place_api, name="save_place_api"),
    path("api/get_saved_places/", views.get_saved_places, name="get_saved_places"),
]
