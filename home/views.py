from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the Index page """
    return render(request, 'home/index.html')


def privacy_policy(request):
    """ A view to return the Privacy Policy page """
    return render(request, 'home/privacy_policy.html')


def help_page(request):
    """ A view to return the Help/FAQs page """
    return render(request, 'home/help_page.html')


def contact_page(request):
    """ A view to return the Contact us page """
    return render(request, 'home/contact_page.html')


def about_page(request):
    """ A view to return the About us page """
    return render(request, 'home/about_page.html')
