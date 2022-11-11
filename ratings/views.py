from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def ratings(request, order_number, product_id):
    """ A view to return the Index page """
    return render(request, 'ratings/rate_item.html')