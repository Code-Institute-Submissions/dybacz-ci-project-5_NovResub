from django.contrib import admin
from .models import Voucher


# Register your models here.
class VoucherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'voucher_code',
        'fractional_discount',
        'expiry_date',
    )


admin.site.register(Voucher, VoucherAdmin)
