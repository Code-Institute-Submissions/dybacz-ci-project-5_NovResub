""" Context Processor - Make context available
 to all templates across the application """

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ 
    Context used acrossall templates for basket items and active voucher codes
    """

    basket_items = []
    total = 0
    product_count = 0
    voucher = False
    voucher_multiplier = 0
    basket = request.session.get('basket', {})
    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    vouchers = request.session.get('vouchers', {})
    for voucher_id, voucher_data in vouchers.items():
        if isinstance(voucher_data, str):
            voucher_multiplier = Decimal(voucher_data)
            voucher = True

    if voucher:
        grand_total = grand_total - (grand_total * voucher_multiplier)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'voucher': voucher,
        'voucher_multiplier': voucher_multiplier
    }

    return context
