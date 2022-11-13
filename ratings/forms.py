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
            'rating': 'Rating (0-5)',
        }

        self.fields['rating'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'rating':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = f'Your Rating for {self.instance.product.name}'
            else:
                self.fields[field].label  = False
                self.fields[field].widget.attrs['hidden'] = True
                self.fields[field].widget.attrs['class'] = 'disabled hidden'
