from django.db import models
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

# Профиль пользователя.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )

    telephone_number = models.CharField(max_length=12)
    telegram_id = models.IntegerField(blank=True, null=True)
    chat_id = models.IntegerField(blank=True, null=True)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    telephone_number = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
