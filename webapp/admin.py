from django.contrib import admin

from .models import ArticleOrder, Order


# Register your models here.
@admin.register(ArticleOrder)
class ArticleOrder(admin.ModelAdmin):
    list_display = ("profile", "article", "size", "amount")


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("profile", )
