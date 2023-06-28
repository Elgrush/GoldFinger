from django.db import models
from django.conf import settings


# Профиль пользователя.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )
    telegram_id = models.IntegerField(blank=True, null=True)
    chat_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name



# Выполненные заказы пользователя.
class Order(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    jewelery = models.JSONField()

    def __str__(self):
        return self.name


#Запрос по-артикулу
class Jewelery_Request(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.RESTRICT
    )
    article_number = models.IntegerField()
    jewelery_size = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
