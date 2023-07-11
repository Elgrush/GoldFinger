from django.contrib import admin
from .models import ArticleRequestAnswer

from .models import ArticleRequest, Order, Factory, JeweleryType


# Register your models here.
@admin.register(ArticleRequest)
class ArticleRequest(admin.ModelAdmin):
    list_display = ("user", "article", "type", "size", "amount", "factory", "created_at", "updated_at")


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")


@admin.register(Factory)
class Factory(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ArticleRequestAnswer)
class ArticleRequestAnswerAdmin(admin.ModelAdmin):
    list_display = ("request", "amount", "created_at")


@admin.register(JeweleryType)
class JeweleryType(admin.ModelAdmin):
    list_display = ("name",)
