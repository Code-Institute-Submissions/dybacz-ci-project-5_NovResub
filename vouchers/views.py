from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import AdminVoucherForm


from .models import Voucher

# Create your views here.
@login_required
def voucher_admin(request):
    """ A view to return the voucher admin page """

    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required \
        permissions to do that.')
        return redirect(reverse('home'))
    
    vouchers = Voucher.objects.all()
    template = 'vouchers/voucher_admin.html'
    context = {
        'profile_page': True,
        'vouchers': vouchers
    }

    return render(request, template, context)


@login_required
def add_voucher(request):
    """ Add a new voucher to the store """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required \
            permissions to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdminVoucherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success : Voucher Added')
            return redirect(reverse('voucher_admin'))
        else:
            messages.error(request, 'Error: Failed to add voucher. Please make \
                sure the form is valid.')
    else:
        form = AdminVoucherForm()

    template = 'vouchers/add_voucher.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_voucher(request, voucher_id):
    """ Edit an voucher """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required \
            permissions to do that.')
        return redirect(reverse('home'))

    voucher = get_object_or_404(Voucher, pk=voucher_id)
    if request.method == 'POST':
        form = AdminVoucherForm(request.POST, instance=voucher)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success: {voucher.name} Updated!')
            return redirect(reverse('voucher_admin'))
        else:
            messages.error(request, f'Error: Failed to update {voucher.name}. \
                Please make sure the form is valid')
    else:
        form = AdminVoucherForm(instance=voucher)
        messages.info(request, f'Currently Editing Voucher: {voucher.name}')

    template = 'vouchers/edit_voucher.html'
    context = {
        'form': form,
        'voucher': voucher,
    }
    return render(request, template, context)


@login_required
def remove_voucher(request, voucher_id):
    """" Remove voucher """
    if not request.user.is_staff:
        messages.error(request, 'Access Denied: You do not have the required \
            permissions to do that.')
        return redirect(reverse('home'))

    voucher = get_object_or_404(Voucher, pk=voucher_id)
    voucher.delete()
    messages.success(request, f'{voucher.name} - Voucher deleted!')
    return redirect(reverse('voucher_admin'))
