from django.db import models
from webapp.models import ArticleRequest
from django import forms


# Create your models here.
class ArticleRequestForm(forms.ModelForm):
    field_order = ["profile"]
    profile = forms.CharField()

    class Meta:
        model = ArticleRequest
        fields = ["article", "size", "amount", "factory"]

    def show(self, model):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True
        self.initial['profile'] = model.profile
        self.initial['article'] = model.article
        self.initial['size'] = model.size
        self.initial['amount'] = model.amount
        self.initial['factory'] = model.factory

        self.fields['profile'].label = "Ник:"
        self.fields['article'].label = "Артикул:"
        self.fields['size'].label = "Размер:"
        self.fields['amount'].label = "Количество:"
        self.fields['factory'].label = "Завод изготовитель:"
