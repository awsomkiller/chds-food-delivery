import uuid
from django.db import models
from apps.users.models import User


class Transaction(models.Model):
    ORDER_TYPE_CHOICES = [
        ('WALLET_RECHARGE', 'Wallet Recharge'),
        ('FOOD_ORDER', 'Food Order'),
    ]

    TRANSACTION_FROM_CHOICES = [
        ('WALLET', 'Wallet'),
        ('STRIPE', 'Stripe'),
    ]

    OPERATION_TYPE_CHOICES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('requires_payment_method', 'Requires Payment Method'),
        ('requires_confirmation', 'Requires Confirmation'),
        ('requires_action', 'Requires Action'),
        ('processing', 'Processing'),
        ('succeeded', 'Succeeded'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='aud')
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True)
    transaction_from = models.CharField(max_length=10, choices=TRANSACTION_FROM_CHOICES)
    operation_type = models.CharField(max_length=10, choices=OPERATION_TYPE_CHOICES)
    stripe_payment_intent_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    stripe_charge_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES, default='requires_payment_method')
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    payment_method_details = models.JSONField(null=True, blank=True)
    receipt_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.order_type} ({self.operation_type})"



class WalletCoupon(models.Model):
    recharge_amount = models.DecimalField(max_digits=10, decimal_places=2)
    recharge_value = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Wallet Coupon"
        verbose_name_plural = "Wallet Coupons"
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} (Code: {self.code})"


class OrderCoupon(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('PERCENTAGE', 'Percentage'),
        ('FIXED', 'Fixed'),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_upto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order Coupon"
        verbose_name_plural = "Order Coupons"
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} (Code: {self.code})"
