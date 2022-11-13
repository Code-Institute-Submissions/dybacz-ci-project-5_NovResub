from django.urls import path
from . import views

urlpatterns = [
    path('my_ratings/', views.my_ratings, name='my_ratings'),
    path('my_ratings/<str:order_number>/<int:product_id>', views.ratings, name='product_rating'),
]
