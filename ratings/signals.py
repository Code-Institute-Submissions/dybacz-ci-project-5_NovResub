from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserItemRatingLine


@receiver(post_save, sender=UserItemRatingLine)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update rating total on lineitem update/create
    """
    instance.item_rating.update_total_rating()
    instance.product.rating = instance.item_rating.total_rating
    instance.product.save()


@receiver(post_delete, sender=UserItemRatingLine)
def update_on_delete(sender, instance, **kwargs):
    """
    Update rating total on lineitem update/create
    """
    instance.item_rating.update_total_rating()
