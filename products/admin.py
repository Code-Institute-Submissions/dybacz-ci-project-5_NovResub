from django.contrib import admin
from .models import Product, MainCategory, SubCategory

# Register your models here.


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'main_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
