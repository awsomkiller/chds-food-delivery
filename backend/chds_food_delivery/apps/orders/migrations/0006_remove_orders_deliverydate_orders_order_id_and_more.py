# Generated by Django 5.1.3 on 2024-11-26 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_merge_20241123_1836'),
        ('transactions', '0003_transaction_created_at_transaction_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='deliverydate',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='schedule_date',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Schedule Date'),
        ),
        migrations.AddField(
            model_name='orders',
            name='time_slot',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Time Slot'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='pickup_location',
            field=models.TextField(default='NA', verbose_name='Pickup Location'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('ORDER_PLACED', 'Order Placed'), ('PAYMENT_SUCCESS', 'Payment Success'), ('PAYMENT_FAILED', 'Payment Failed'), ('READY_FOR_PICKUP', 'Ready for Pickup'), ('OUT_FOR_DELIVERY', 'Out for Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='ORDER_PLACED', max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction'),
        ),
    ]