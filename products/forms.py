fromdjango import forms
from .models import Product, MainCategory, SubCategory


class AdminProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_categories = MainCategory.objects.all()
        sub_categories = SubCategory.objects.all()
        mc_friendly_names = [(mc.id, mc.get_friendly_name()) for mc in main_categories]
        self.fields['main_category'].choices = mc_friendly_names
        sc_friendly_names = [(sc.id, sc.get_friendly_name()) for sc in sub_categories]
        self.fields['sub_category'].choices = sc_friendly_names

        for field_name, fields in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'



