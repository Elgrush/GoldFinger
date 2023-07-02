from django.db import models
from authorisation.models import UserProfile

# Выполненные заказы пользователя.
class Order(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    jewelery = models.JSONField()

    def __str__(self):
        return self.name


# Запрос по-артикулу
class JeweleryRequest(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    article_number = models.IntegerField()
    jewelery_size = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
