from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('help/', views.help_page, name='help_page'),
    path('contact-us/', views.contact_page, name='contact_page'),
    path('about-us/', views.about_page, name='about_page'),
]
