# Generated by Django 3.0.1 on 2022-11-12 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_rating_collection'),
        ('ratings', '0003_auto_20221112_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrating',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
