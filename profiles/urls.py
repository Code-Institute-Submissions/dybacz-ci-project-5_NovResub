from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_orders/order_history', views.my_orders, name='my_orders'),
    path('my_orders/order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
