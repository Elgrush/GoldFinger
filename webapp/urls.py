from django.urls import path, include

from . import views

urlpatterns = [
    path("dispatcher/", include("dispatcher.urls")),
    path("", views.index, name="index")
]
