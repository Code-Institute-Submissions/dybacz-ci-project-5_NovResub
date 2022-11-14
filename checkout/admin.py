from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Admin for Order Line Items """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Admin for Orders"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid', 'user_profile',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city',
              'street_address1', 'street_address2',
              'county', 'delivery_cost', 'order_total',
              'grand_total', 'original_basket', 'stripe_pid', 'user_profile',
              'voucher_info')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
