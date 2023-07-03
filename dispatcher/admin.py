from django.contrib import admin

from .models import JeweleryRequest, Order


# Register your models here.
myModels = [JeweleryRequest, Order]  # iterable list
admin.site.register(myModels)
