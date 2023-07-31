from django.contrib.auth.models import User
from django.db import models


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


class JeweleryType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Factory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ArticleRequest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE

    )
    article = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    amount = models.IntegerField(null=True, blank=True)
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        JeweleryType,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_answers(self):
        return ArticleRequestAnswer.objects.filter(request=self)

    def get_answer(self):
        last_answer = None
        for i in ArticleRequestAnswer.objects.filter(
                request=ArticleRequest.objects.get(
                    id=self.id)):
            last_answer = i
        return last_answer

    def __str__(self):
        return self.article


class ArticleRequestAnswer(models.Model):
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.OneToOneField(
        ArticleRequest,
        on_delete=models.CASCADE
    )


class CatalogItem(models.Model):
    article = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    amount = models.IntegerField(null=True, blank=True)

    def images(self):
        try:
            return map(len(), CatalogItemImage.objects.filter(CatalogItem=self))
        except None:
            return None


class CatalogItemImage(models.Model):
    CatalogItem = models.ForeignKey(CatalogItem, related_name='images', on_delete=
    models.CASCADE)
    image = models.ImageField(upload_to="images")
