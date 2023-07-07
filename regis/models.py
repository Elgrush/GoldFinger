from django.db import models
from django import forms
from webapp.models import ArticleRequestForm, Factory, ArticleRequest


# Create your models here.
class ArticleRequestAnswer(models.Model):
    size = models.CharField(max_length=150)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE
    )
    request = models.ForeignKey(
        ArticleRequest,
        on_delete=models.CASCADE
    )


class ArticleRequestAnswerForm(forms.ModelForm):
    request_id = forms.IntegerField()

    class Meta:
        model = ArticleRequestAnswer
        fields = ["size", "amount", "factory"]
