from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_plans, name='view_plans'),
]
