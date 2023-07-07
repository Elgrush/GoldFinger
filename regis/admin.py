from django.contrib import admin
from .models import ArticleRequestAnswer


# Register your models here.
@admin.register(ArticleRequestAnswer)
class ArticleRequestAnswerAdmin(admin.ModelAdmin):
    list_display = ("size", "amount", "factory", "request", "created_at")
