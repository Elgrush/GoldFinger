from django.contrib import admin

from .models import UserProfile, PickupAddress, ShoppingCartOrder


class ShoppingCartOrderInline(admin.TabularInline):
    model = ShoppingCartOrder
    extra = 1


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "surname", "middle_name", "telephone_number")
    inlines = [ShoppingCartOrderInline, ]


@admin.register(PickupAddress)
class PickupAddressAdmin(admin.ModelAdmin):
    list_display = ("profile", "address")
