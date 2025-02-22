# Generated by Django 5.1.3 on 2024-11-16 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Menu Category',
                'verbose_name_plural': 'Menu Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Resturant Name')),
                ('location', models.CharField(max_length=255, verbose_name='Resturant Location')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Resturant Code')),
                ('from_time', models.TimeField(verbose_name='Opening Time')),
                ('to_time', models.TimeField(verbose_name='Closing Time')),
                ('status', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off')], default='OFF', max_length=3, verbose_name='Resturant Status')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Contact Number')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('calories', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('carbs', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='restaurants.menucategory')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('is_main', models.BooleanField(default=False)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restaurants.menuitem')),
            ],
            options={
                'verbose_name': 'Menu Image',
                'verbose_name_plural': 'Menu Images',
                'ordering': ['-is_main'],
            },
        ),
    ]
