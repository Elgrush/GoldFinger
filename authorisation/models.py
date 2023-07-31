from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


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

    def __str__(self):
        return self.user.username


# Адресс самовывоза
class PickupAddress(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=1023)

    def __str__(self):
        return self.profile.user.username
