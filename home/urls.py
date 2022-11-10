from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('help/', views.help_page, name='help_page'),
]
