from django.urls import path
from . import views

urlpatterns = [
    path('<str:order_number>/<int:product_id>', views.ratings, name='product_rating'),
]
