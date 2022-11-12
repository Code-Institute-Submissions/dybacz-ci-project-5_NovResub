from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db.models import Avg


from products.models import Product
from checkout.models import Order, OrderLineItem


class ItemRating(models.Model):
    """
    Item rating model for all user ratings.
    """
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True, blank=True)
    total_rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)

    def update_total_rating(self):
        """
        Update item rating each time a line item is added.
        """

        self.total_rating = self.lineitems.aggregate(
            Avg('rating'))['rating__avg'] or 0
        self.save()

    def __str__(self):
        return f'{self.product} - Rating: {self.total_rating}'


class UserItemRatingLine(models.Model):
    """
    User rating model for items purchased.
    """
    item_rating = models.ForeignKey(ItemRating, null=False,
                                    blank=False, on_delete=models.CASCADE,
                                    related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True,
                                related_name='product')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name='user')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name='order')
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(0), MaxValueValidator(5)
        ])

    def __str__(self):
        return f'{self.rating} / 5 review from {self.user.username}\
    on order {self.order.order_number}'

@receiver(post_save, sender=Product)
def create_product_rating_collection(sender, instance, created, **kwargs):
    if created:
        collection = ItemRating.objects.create(product=instance)
        print(collection, collection.pk, collection.product.rating_collection)
        Product.objects.filter(pk=instance.pk).update(rating_collection=collection)
        print(collection, collection.pk, collection.product.rating_collection)


@receiver(post_save, sender=OrderLineItem)
def create_product_rating_instance(sender, instance, created, **kwargs):
    """
    Create Instance for rating product from order for each order line item
    """
    if created:
        UserItemRatingLine.objects.create(
            item_rating=instance.product.rating_collection,
            product=instance.product,
            user=instance.order.user_profile.user,
            order=instance.order
        )
