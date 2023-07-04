from django.contrib import admin

from .models import ArticleRequest, Order, Factory


# Register your models here.
@admin.register(ArticleRequest)
class ArticleRequest(admin.ModelAdmin):
    list_display = ("profile", "article", "size", "amount")


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("profile", )


@admin.register(Factory)
class Factory(admin.ModelAdmin):
    list_display = ("name", )
