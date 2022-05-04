from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, MainCategory, SubCategory

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    main_categories = None
    sub_categories = None

    if request.GET:
        # if 'main_category' in request.GET:
        #     main_categories = request.GET['main_category'].split('&&')
        #     products = products.filter(main_category__name__in=main_categories)
        #     main_categories = MainCategory.objects.filter(
        #         name__in=main_categories)

        if 'main_category' in request.GET and 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category'].split('&&')
            main_categories = request.GET['main_category'].split('&&')
            products = products.filter(
                main_category__name__in=main_categories,
                sub_category__name__in=sub_categories)
            main_categories = MainCategory.objects.filter(
                name__in=main_categories)
            sub_categories = SubCategory.objects.filter(
                name__in=sub_categories)

        elif 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category'].split('&&')
            products = products.filter(sub_category__name__in=sub_categories)
            sub_categories = SubCategory.objects.filter(
                name__in=sub_categories)
        else:
            main_categories = request.GET['main_category'].split('&&')
            products = products.filter(main_category__name__in=main_categories)
            main_categories = MainCategory.objects.filter(
                name__in=main_categories)


        if 'product_query' in request.GET:
            query = request.GET['product_query']
            if not query:
                messages.error(request,"You didn't any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_main_categories': main_categories,
        'current_sub_categories': sub_categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
