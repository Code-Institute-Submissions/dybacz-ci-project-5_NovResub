from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404, get_list_or_404
)
from django.contrib import messages
import json
from products.models import Product
from vouchers.models import Voucher

# Create your views here.


def view_basket(request):
    """ A view to return the basket contents page """
    voucher_session = request.session.get('vouchers', {})
    voucher_id = None
    # print(voucher_session.get('1'))
    for key, value in voucher_session.items():
        voucher_id = key
    
    if voucher_id != None:
        voucher_item = get_object_or_404(Voucher, pk=voucher_id)
    else:
        voucher_item = None
    

    context = {
        'view_basket': True,
        'voucher_item': voucher_item
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """ Add a quanitity of the specified prodcut to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'An additional {quantity} x {product.name}:\
                         Size: {size.upper()} has been added to your basket')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'{quantity} x {product.name}:\
                         Size: {size.upper()} added to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'{quantity} x {product.name}:\
                     Size: {size.upper()} added to your basket')

    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request, f'An additional {quantity} x {product.name} has been \
                    added to your basket')
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'{quantity} x {product.name} added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quanitity of the specified prodcut in the shopping basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(
                    request, f'{product.name}: Size: {size.upper()} quantity \
                        updated to {quantity}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(
                    request, f'{product.name}: Size: {size.upper()} removed \
                        from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(
                request, f'{product.name} quantity updated to {quantity} in \
                    your basket')
        else:
            basket.pop(item_id)
            messages.success(
                request, f'{product.name} removed from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove the item from the shopping basket """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        size_from_post = json.load(request)['product_size']
        if size_from_post:
            size = size_from_post
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(
                    request, f'All {product.name}: Size: {size.upper()} \
                        removed from your basket')
        else:
            basket.pop(item_id)
            messages.success(
                request, f'All {product.name} removed from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as basket_error:
        messages.error(
            request, f'Error removing item from basket: {basket_error}')
        return HttpResponse(status=500)
