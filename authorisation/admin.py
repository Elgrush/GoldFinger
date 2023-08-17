from django.contrib import admin

from .models import UserProfile, PickupAddress, ShoppingCartOrder, ShoppingCartRequest


class ShoppingCartOrderInline(admin.TabularInline):
    model = ShoppingCartOrder
    extra = 1


class ShoppingCartRequestInline(admin.TabularInline):
    model = ShoppingCartRequest
    extra = 1


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "surname", "middle_name", "telephone_number")
    inlines = [ShoppingCartOrderInline, ShoppingCartRequestInline]


@admin.register(PickupAddress)
class PickupAddressAdmin(admin.ModelAdmin):
    list_display = ("profile", "address")
