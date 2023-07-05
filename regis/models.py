from django.db import models
from webapp.models import ArticleRequest
from django import forms


# Create your models here.
class ArticleRequestForm(forms.ModelForm):
    field_order = ["user"]
    user = forms.CharField()

    class Meta:
        model = ArticleRequest
        fields = ["article", "size", "amount", "factory"]

    factory = forms.CharField()

    def show(self, model):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True
        self.initial['user'] = model.user
        self.initial['article'] = model.article
        self.initial['size'] = model.size
        self.initial['amount'] = model.amount
        self.initial['factory'] = model.factory

        self.fields['user'].label = "Ник:"
        self.fields['article'].label = "Артикул:"
        self.fields['size'].label = "Размер:"
        self.fields['amount'].label = "Количество:"
        self.fields['factory'].label = "Завод изготовитель:"
