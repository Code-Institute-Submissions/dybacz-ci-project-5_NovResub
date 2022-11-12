from django import forms
from .models import UserItemRatingLine


class UserItemRatingForm(forms.ModelForm):
    """"""
    class Meta:
        """"""
        model = UserItemRatingLine
        fields = {'product', 'order', 'rating',}

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Ordered Product:',
            'order': 'Order Number:',
            'rating': 'Rating (0-5)',
        }

        self.fields['rating'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if field != 'country':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #         self.fields[field].widget.attrs['class'] = 'stripe-style-input \
        #             my-2'
        #     else:
        #         self.fields[field].widget.attrs['class'] = 'stripe-style-input \
        #             my-2 form-select'
        #     self.fields[field].label = False
