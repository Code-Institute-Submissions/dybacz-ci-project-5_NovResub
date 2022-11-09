from django.shortcuts import render


# Create your views here.
def view_plans(request):
    """ A view to return the plans contents page """
    return render(request, 'plans/plans.html')
