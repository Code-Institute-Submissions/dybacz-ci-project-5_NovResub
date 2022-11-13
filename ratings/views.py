from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from products.models import Product
from .models import UserItemRatingLine

from .forms import UserItemRatingForm


# Create your views here.
@login_required
def my_ratings(request):
    """ A view to return the mMy ratings page """

    user_ratings = UserItemRatingLine.objects.all().filter(
        user=request.user, rating__isnull=True
        )

    template = 'ratings/my_ratings.html'
    context = {
        'profile_page': True,
        'ratings': user_ratings,
    }

    return render(request, template, context)


@login_required
def ratings(request, order_number, product_id):
    """ A view to return the rating form page """

    order_number_id = get_object_or_404(Order, order_number=order_number).pk
    print(order_number_id)
    item_rating_line = get_object_or_404(
        UserItemRatingLine,
        user=request.user,
        product=product_id,
        order=order_number_id
    )
    print(item_rating_line)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        product_pk = request.POST.get('product')
        product = get_object_or_404(Product, product=product_pk).name
        form = UserItemRatingForm(request.POST, instance=item_rating_line)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success: You rated {product} as\
             a {rating} /5')
            return redirect(reverse(
                'my_ratings'))
        else:
            messages.error(request, 'Error: Rating submission failed, Please make sure the \
                form is valid')
    else:
        form = UserItemRatingForm(instance=item_rating_line)

    template = 'ratings/rate_item.html'
    context = {
        'form': form,
        'profile_page': True,
        'item': item_rating_line,
    }

    return render(request, template, context)
