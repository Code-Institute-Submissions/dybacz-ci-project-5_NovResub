from django.urls import path
from . import views

urlpatterns = [
    path('', views.voucher_admin, name='voucher_admin'),
    path('add_voucher/', views.add_voucher, name='add_voucher'),
    path('edit_voucher/<int:voucher_id>>',
         views.edit_voucher,
         name='edit_voucher'),
    path('remove_voucher/<int:voucher_id>',
         views.remove_voucher,
         name='remove_voucher'),
    path('voucher_attempt/', views.voucher_attempt, name='voucher_attempt'),

]
