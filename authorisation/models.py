from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from webapp.models import CatalogItem, ArticleRequestAnswer


# Create your models here.

# Профиль пользователя.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(blank=True, max_length=150)
    surname = models.CharField(blank=True, max_length=150)
    middle_name = models.CharField(blank=True, max_length=150)

    telephone_number = PhoneNumberField(null=False, blank=False)
    address = models.CharField(default=None, blank=True, null=True, max_length=1023)

    def get_catalog_cart(self):
        return ShoppingCartOrder.objects.filter(UserProfile=self)

    def get_request_cart(self):
        return ShoppingCartRequest.objects.filter(UserProfile=self)

    def __str__(self):
        return self.user.username


class ShoppingCartOrder(models.Model):
    amount = models.IntegerField()
    UserProfile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    CatalogItem = models.ForeignKey(
        CatalogItem,
        on_delete=models.CASCADE
    )


class ShoppingCartRequest(models.Model):
    amount = models.IntegerField()
    UserProfile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    ArticleRequestAnswer = models.ForeignKey(
        ArticleRequestAnswer,
        on_delete=models.CASCADE
    )


# Адресс самовывоза
class PickupAddress(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=1023)

    def __str__(self):
        return self.profile.user.username
