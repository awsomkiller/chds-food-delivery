# Generated by Django 5.1.3 on 2024-11-27 00:24

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transaction_created_at_transaction_currency_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('currency', models.CharField(default='aud', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='digital_wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]