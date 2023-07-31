from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu, name='reg/menu'),
    path('create_lot/', views.create_lot, name='reg/create_lot'),
] + static('edit_lot/', document_root=settings.MEDIA_ROOT)
