from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty at the momet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LRHpTHnWi2pmNwaIY5GzzIJ4Nr7zEbysEPkfRjnlxx62uJquB4jI5Ng5t5Ws56D2FTdorkZuGsh7OsNUiD3Ye5U00BnDPlF6p',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
