from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("confirm/", views.confirm, name="confirm"),
    path("edit_form/", views.edit_form, name="edit_form"),
    path("order_history/", views.order_history, name="order_history"),
    path("request_history/", views.request_history, name="request_history"),
    path("catalog/", views.catalog, name="catalog")
]
