from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, MainCategory, SubCategory


class AdminProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = {'rating', 'image_url', 'rating_collection', }

    image = forms.ImageField(label="Image", required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_categories = MainCategory.objects.all()
        sub_categories = SubCategory.objects.all()
        mc_friendly_names = [
            (mc.id, mc.get_friendly_name()) for mc in main_categories
            ]
        self.fields['main_category'].choices = mc_friendly_names
        sc_friendly_names = [
            (sc.id, sc.get_friendly_name()) for sc in sub_categories
            ]
        self.fields['sub_category'].choices = sc_friendly_names

        for field_name, field in self.fields.items():
            if field_name != 'main_category':
                field.widget.attrs['class'] = 'border-primary mb-2'
            else:
                field.widget.attrs['class'] = 'border-primary mb-2 form-select'
