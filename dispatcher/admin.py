from django.contrib import admin

from .models import JeweleryRequest, Order


# Register your models here.
@admin.register(JeweleryRequest)
class JeweleryRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "jewelery",]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "article_number", "jewelery_size", "amount",]
