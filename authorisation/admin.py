from django.contrib import admin

from .models import UserProfile, PickupAddress


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "telephone_number")


@admin.register(PickupAddress)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("profile", "address")
