# Generated by Django 5.1.3 on 2024-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orders_shipping_charges_orders_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Cooking Instructions'),
        ),
    ]
