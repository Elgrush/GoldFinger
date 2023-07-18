from django.contrib import admin
from .models import ArticleRequestAnswer
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from .models import ArticleRequest, Order, Factory, JeweleryType, CatalogItem


# Register your models here.
@admin.register(ArticleRequest)
class ArticleRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "article", "type", "size", "amount", "factory", "created_at", "updated_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ArticleRequestAnswer)
class ArticleRequestAnswerAdmin(admin.ModelAdmin):
    list_display = ("request", "amount", "created_at")


@admin.register(JeweleryType)
class JeweleryTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ("article", "size", "photo")


@receiver(pre_delete, sender=CatalogItem)
def CatalogItem_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo.delete(False)
