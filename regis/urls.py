from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('answer_request/', views.answer_request, name='answer_request')
]