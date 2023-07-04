from django.db import models
from webapp.models import ArticleOrder
from django import forms


# Create your models here.
class ArticleRequest(forms.Form):
    class Meta:
        model = ArticleOrder
        fields = ["profile", "article", "size", "amount"]
