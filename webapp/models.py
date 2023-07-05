from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


# Выполненные заказы пользователя.
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.name


# Запрос по-артикулу


class Factory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ArticleRequest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE

    )
    article = models.CharField(max_length=31)
    size = models.CharField(max_length=150)
    amount = models.IntegerField()
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article


class ArticleRequestForm(forms.Form):
    article = forms.CharField(label="Артикул:")
    size = forms.CharField(label="Размер изделий:")
    amount = forms.IntegerField(label="Количество изделий:")
    factory = forms.ChoiceField(choices=((i, Factory.objects.all()[i].name) for i in range(len(Factory.objects.all()))))
    locked = False

    def __init__(self, *args, **kwargs):
        super(ArticleRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"

    def lock(self):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

    def is_lock(self):
        self.locked = True
        for field in self.fields:
            try:
                if not self.fields[field].widget.attrs['readonly']:
                    self.locked = False
                    return self.locked
            except KeyError:
                self.locked = False
                return self.locked
