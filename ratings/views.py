from django.shortcuts import render, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserItemRatingForm
from .models import UserItemRatingLine

# Create your views here.
@login_required
def my_ratings(request):
    """ A view to return the mMy ratings page """

    user_ratings = UserItemRatingLine.objects.all().filter(user=request.user)

    template = 'ratings/my_ratings.html'
    context = {
        'profile_page': True,
        'ratings': user_ratings,
    }

    return render(request, template, context)


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
