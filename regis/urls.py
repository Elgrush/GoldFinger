from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='reg/menu'),
    path('create_lot/', views.create_lot, name='reg/create_lot'),
]