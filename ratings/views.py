from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserItemRatingForm

# Create your views here.
@login_required
def ratings(request, order_number, product_id):
    """ A view to return the Index page """

    form = UserItemRatingForm()

    template = 'ratings/rate_item.html'
    context = {
        'form': form,
        'profile_page': True,
    }

    return render(request, template, context)