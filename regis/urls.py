from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu, name='reg/menu'),
    path('create_lot/', views.create_lot, name='reg/create_lot'),
    path('edit_lot/', views.edit_lot, name='reg/edit_lot'),
    path('delete_lot/', views.delete_lot, name='reg/delete_lot'),
    path('delete_image/', views.delete_image, name='reg/delete_image'),
] + static('edit_lot/', document_root=settings.MEDIA_ROOT) + static('delete_lot/', document_root=settings.MEDIA_ROOT)
