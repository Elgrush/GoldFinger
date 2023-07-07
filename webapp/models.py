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
    size = models.IntegerField()
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
    field_order = ["factory"]

    article = forms.CharField(label="Артикул:")
    size = forms.IntegerField(label="Размер изделий:")
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


class ArticleRequestShowForm(forms.ModelForm):
    field_order = ["factory", "user"]
    user = forms.CharField()
    request_time = forms.CharField()
    answer_time = forms.CharField()
    ArticleRequestId = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'display: none'}), label="")

    class Meta:
        model = ArticleRequest
        fields = ["article", "size", "amount", "factory"]

    factory = forms.CharField()

    def hide_user(self):
        self.fields['user'].widget.attrs.update({'style': 'display: none'})
        self.fields['user'].label = ""

    def show(self, model):
        self.initial['user'] = model.user
        self.initial['article'] = model.article
        self.initial['size'] = model.size
        self.initial['amount'] = model.amount
        self.initial['factory'] = model.factory
        self.initial['request_time'] = str(model.created_at).split('.')[0]
        self.initial['answer_time'] = str(model.updated_at).split('.')[0]
        if model.created_at == model.updated_at:
            self.initial['answer_time'] = "Ещё в обработке"
        self.initial['ArticleRequestId'] = model.id

        self.fields['user'].label = "Ник:"
        self.fields['article'].label = "Артикул:"
        self.fields['size'].label = "Размер:"
        self.fields['amount'].label = "Количество:"
        self.fields['factory'].label = "Завод изготовитель:"
        self.fields['request_time'].label = "Время создания"
        self.fields['answer_time'].label = "Ответ"

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True
