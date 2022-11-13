from django import forms
from .models import Voucher


class AdminVoucherForm(forms.ModelForm):

    class Meta:
        model = Voucher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """    """
        placeholders = {
            'name': 'Voucher Name',
            'description': 'Description',
            'voucher_code': 'Code (max 12 char)',
            'fractional_discount': 'Discount Multiplier',
            'expiry_date': 'Expiry Date',
        }
        super().__init__(*args, **kwargs)

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-primary mb-2'
            if self.fields[field].widget.attrs['placeholder'] == 'Expiry Date':
                self.fields[field].widget.input_type = "date"
