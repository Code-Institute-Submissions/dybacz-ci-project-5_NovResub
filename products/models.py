from django.db import models

# Create your models here.


class MainCategory(models.Model):
    """"""

    class Meta:
        verbose_name_plural = 'Main Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class SubCategory(models.Model):
    """"""

    class Meta:
        verbose_name_plural = 'Sub Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Product(models.Model):
    """"""
    main_category = models.ForeignKey(
        'MainCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ManyToManyField(
        'SubCategory', blank=True)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rating_collection = models.ForeignKey('ratings.ItemRating', null=True,
                                          blank=True, on_delete=models.CASCADE,
                                          related_name='rating_collection')

    def __str__(self):
        return str(self.name)
