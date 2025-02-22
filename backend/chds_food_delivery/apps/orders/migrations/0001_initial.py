# Generated by Django 5.1.3 on 2024-11-18 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0002_menuitem_price'),
        ('transactions', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(verbose_name='Order Time')),
                ('delivery_time', models.DateTimeField(verbose_name='Delivery Time')),
                ('status', models.CharField(choices=[('ORDER_PREPARING', 'Order Preparing'), ('PACKED', 'Packed'), ('READY_FOR_PICKUP', 'Ready for Pickup'), ('SHIPPED', 'Shipped'), ('OUT_FOR_DELIVERY', 'Out for Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu_item', models.JSONField(help_text='Selected Menu items Json object', verbose_name='Menu Items')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='restaurants.restaurant')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userorders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-order_time'],
            },
        ),
    ]
