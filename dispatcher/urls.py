from django.urls import path

from . import views

urlpatterns = [
    path('makeArticleRequest/', views.read_article_request, name="article")
]
