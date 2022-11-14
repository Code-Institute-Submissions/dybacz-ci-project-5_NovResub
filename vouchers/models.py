from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Voucher(models.Model):
    """
    Voucher model for all voucher details.
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    voucher_code = models.CharField(max_length=12)
    fractional_discount = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(1)]
        )
    expiry_date = models.DateField()

    def __str__(self):
        return f'{self.name}'
