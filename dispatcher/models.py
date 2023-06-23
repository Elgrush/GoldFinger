from django.db import models
from django.conf import settings


# Профиль пользователя.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )


# Выполненные заказы пользователя.
class Order(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    jewelery = models.JSONField()


#Запрос по-артикулу
class Jewelery_Request(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    article_number = models.IntegerField()
    jewelery_size = models.IntegerField()
    amount = models.IntegerField()
