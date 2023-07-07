from django.db import models
from django import forms
from webapp.models import ArticleRequestForm, Factory, ArticleRequest


# Create your models here.
class ArticleRequestAnswer(models.Model):
    size = models.IntegerField()
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
    ArticleRequestId = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'display: none'}), label="")

    class Meta:
        model = ArticleRequestAnswer
        fields = ["size", "amount", "factory"]

    def __init__(self, *args, **kwargs):
        super(ArticleRequestAnswerForm, self).__init__(*args, **kwargs)
        self.fields['size'].label = "Размер:"
        self.fields['amount'].label = "Количество:"
        self.fields['factory'].label = "Завод изготовитель:"
