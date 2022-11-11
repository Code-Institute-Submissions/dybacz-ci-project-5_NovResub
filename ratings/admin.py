from django.contrib import admin
from .models import UserItemRatingLine, ItemRating


# Register your models here.
class UserItemRatingLineAdminInLine(admin.TabularInline):

    model = UserItemRatingLine
    # readonly_fields = ('product', 'rating', 'user', 'order')


class ItemRatingAdmin(admin.ModelAdmin):
    """"""
    inlines = (UserItemRatingLineAdminInLine,)
    list_display = ('product', 'total_rating',)


admin.site.register(ItemRating, ItemRatingAdmin)
