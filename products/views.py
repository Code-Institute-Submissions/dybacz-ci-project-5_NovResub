from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, MainCategory, SubCategory
from .forms import AdminProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    main_categories = None
    sub_categories = None
    sort = None
    direction = None

    if request.GET:
        # if 'main_category' in request.GET:
        #     main_categories = request.GET['main_category'].split('&&')
        #     products = products.filter(main_category__name__in=main_categories)
        #     main_categories = MainCategory.objects.filter(
        #         name__in=main_categories)

        if 'main_category' in request.GET and 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category'].split('%')
            main_categories = request.GET['main_category'].split('%')
            products = products.filter(
                main_category__name__in=main_categories,
                sub_category__name__in=sub_categories)
            main_categories = MainCategory.objects.filter(
                name__in=main_categories)
            sub_categories = SubCategory.objects.filter(
                name__in=sub_categories)

        elif 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category'].split('%')
            products = products.filter(sub_category__name__in=sub_categories)
            sub_categories = SubCategory.objects.filter(
                name__in=sub_categories)
                
        elif 'main_category' in request.GET:
            main_categories = request.GET['main_category'].split('%')
            products = products.filter(main_category__name__in=main_categories)
            main_categories = MainCategory.objects.filter(
                name__in=main_categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'main_category':
                sortkey = 'main_category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'product_query' in request.GET:
            query = request.GET['product_query']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(
                description__icontains=query) | Q(
                main_category__name=query) | Q(
                sub_category__name=query
                )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_main_categories': main_categories,
        'current_sub_categories': sub_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a new product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required permissions to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdminProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Success : Product Added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Error: Failed to add product. Please make sure the form is valid.')
    else:
        form = AdminProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an exisitng product in store """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required permissions to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AdminProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success: {product.name} Updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Error: Failed to update {product.name}. Please make sure the form is valid')
    else:
        form = AdminProductForm(instance=product)
        messages.info(request, f'Currently Editing: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def remove_product(request, product_id):
    """" Remove product from the store """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required permissions to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} deleted!')
    return redirect(reverse('products'))
