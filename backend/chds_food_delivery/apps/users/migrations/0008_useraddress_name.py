# Generated by Django 5.1.3 on 2024-11-26 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
    ]
