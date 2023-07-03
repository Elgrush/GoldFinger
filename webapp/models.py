from django.db import models
from django import forms
from authorisation.models import UserProfile


# Выполненные заказы пользователя.
class Order(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.profile.name


# Запрос по-артикулу
class ArticleOrder(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    article = models.CharField(max_length=31)
    size = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.article


class ArticleOrderForm(forms.Form):
    article = forms.CharField(label="Артикул:")
    size = forms.CharField(label="Размер изделий:", required=False)
    amount = forms.IntegerField(label="Количество изделий:", required=False)

    def __init__(self, *args, **kwargs):
        super(ArticleOrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"
