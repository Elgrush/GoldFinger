from django.contrib import admin

from .models import ArticleRequest, Order, Factory


# Register your models here.
@admin.register(ArticleRequest)
class ArticleRequest(admin.ModelAdmin):
    list_display = ("user", "article", "size", "amount", "factory", "created_at", "updated_at")


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")


@admin.register(Factory)
class Factory(admin.ModelAdmin):
    list_display = ("name", )
