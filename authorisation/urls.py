from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('login/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_account'),
    path('edit_password/', views.edit_password, name='edit_password'),
]