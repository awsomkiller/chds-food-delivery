# admin.py

from django.contrib import admin
from .models import Orders
from apps.transactions.models import Transaction

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'amount', 'order_time')
    search_fields = ('order_id', 'user__username', 'status')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'amount', 'status', 'transaction_from', 'operation_type', 'created_at')
    search_fields = ('transaction_id', 'user__username', 'status', 'stripe_payment_intent_id')
