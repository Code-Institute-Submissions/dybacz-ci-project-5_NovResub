from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import ProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display User Profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery Information Updated \
                Succesfully')
        else:
            messages.error(request, 'Error: Update Failed, Please makesure the \
                form is valid')
    else:
        form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile_page': True,
    }

    return render(request, template, context)


@login_required
def my_orders(request):
    """Display User Order History"""
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/my_orders.html'
    context = {
        'orders': orders,
        'profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'order_history': True,
    }
    return render(request, template, context)
