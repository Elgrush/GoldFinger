from django.db import models
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=1023)

    def __str__(self):
        return self.profile.user.username


class RegistrationForm(UserCreationForm):
    field_order = ['username', 'email',
                   'name', 'surname', 'middle_name', 'telephone_number',
                   'password1', 'password2', "token"]
    email = forms.EmailField(error_messages={
        'required': 'Заполните это поле'
    })
    telephone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                        error_messages={
                                            'invalid': "Номер телефона должен соответствовать стандарту: "
                                                       "'+999999999'. Доступно не более 15 цифр."
                                        }, label="Номер телефона")
    token = forms.CharField(label="Токен приглашения:")
    name = forms.CharField(label="Ваше имя:")
    surname = forms.CharField(label="Ваша фамилия:")
    middle_name = forms.CharField(label="Ваше отчество:")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'telephone_number', "token"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"
        self.fields['username'].label = "Ник:"
        self.fields['password1'].label = "Пароль:"
        self.fields['password2'].label = "Подтвердите пароль:"
        self.fields['username'].help_text = "Не более 150 символов. Только буквы, цифры и @/./+/-/_ " \
                                            "доступны."
        self.fields['password2'].help_text = "Введите тот же пароль для верификации"
        self.fields['password1'].help_text = "<ul><li>Ваш пароль не должен быть похож на другую Вашу личную " \
                                             "информацию.</li><li>Длина пароля хотя бы 8 символов.</li><li>пароль " \
                                             "должен быть разнообразен.</li><li>Пароль не может состоять только из " \
                                             "цифр.</li></ul>"
        self.fields['password1'].error_messages['invalid'] = "<ul><li>Ваш пароль не должен быть похож на другую Вашу " \
                                                             "личную информацию.</li><li>Длина пароля хотя бы 8 " \
                                                             "символов.</li><li>пароль должен быть " \
                                                             "разнообразен.</li><li>Пароль не может состоять только " \
                                                             "из цифр.</li></ul>"


class EditForm(forms.Form):
    email = forms.EmailField(label="Email:")
    name = forms.CharField(label="Ваше имя:")
    surname = forms.CharField(label="Ваша фамилия:")
    middle_name = forms.CharField(label="Ваше отчество:")
    telephone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                        error_messages={
                                            'invalid': "Номер телефона должен соответствовать стандарту: "
                                                       "'+999999999'. Доступно не более 15ти цифр."
                                        }, label="Номер телефона")
    address = forms.CharField(label="Адресс курьерской доставки", required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label="Ник:", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"


class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Старый пароль")

    password1 = forms.CharField(widget=forms.PasswordInput, label="Новый пароль",
                                help_text="<ul><li>Ваш пароль не должен быть похож на другую Вашу личную " \
                                          "информацию.</li><li>Длина пароля хотя бы 8 символов.</li><li>пароль " \
                                          "должен быть разнообразен.</li><li>Пароль не может состоять только из " \
                                          "цифр.</li></ul>")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтвердите новый пароль",
                                help_text="Введите тот же пароль для верификации")

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"
