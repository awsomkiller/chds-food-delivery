# Generated by Django 5.1.3 on 2024-12-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0015_menuitem_trans_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='trans_desc_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Translation Description Code'),
        ),
    ]
