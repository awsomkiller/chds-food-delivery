from django.db import models
from apps.transactions.models import OrderCoupon
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.transactions.models import Transaction
from datetime import datetime


class Orders(models.Model):
    ORDER_STATUS = [
        ("ORDER_PLACED","Order Placed"),
        ("PAYMENT_SUCCESS", "Payment Success"),
        ("PAYMENT_FAILED", "Payment Failed"),
        ("READY_FOR_PICKUP", 'Ready for Pickup'),
        ("OUT_FOR_DELIVERY", 'Out for Delivery'),
        ("DELIVERED", 'Delivered'),
        ("CANCELLED", 'Cancelled'),
    ]
    ORDER_TYPES = [
        ("PICKUP","Pickup"),
        ("DELIVERY","Delivery")
    ]
    pickup_location = models.TextField(_("Pickup Location"), default="NA")
    order_id = models.CharField(max_length=100, unique=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="userorders")
    order_time = models.DateTimeField(_("Order Time"), auto_now_add=True)
    schedule_date = models.CharField(_("Schedule Date"), max_length=50, null=True, blank=True)
    time_slot = models.CharField(_("Time Slot"), max_length=50, null=True, blank=True)
    order_type = models.CharField(_("Order Type"), choices=ORDER_TYPES, max_length=10, null=True)
    delivery_location = models.TextField(_("Delivery Location"),default="NA")
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="ORDER_PLACED")
    amount = models.CharField(_("Amount"), max_length=50, help_text="In Australian Dollars")
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, null=True, blank=True)
    menu_item = models.JSONField(_("Menu Items"), help_text="Selected Menu items Json object")
    shipping_charges = models.CharField(_("Shipping Charges"), max_length=50, help_text="In Australian Dollars",null=True)
    total_price = models.CharField(_("Total Order price"), max_length=50, help_text="In Australian Dollars", null=True)
    discount = models.CharField(_("Total Discount Applied"), max_length=50, help_text="In Australian Dollars", default="0")
    tax = models.CharField(_("Total Tax"), max_length=50, help_text="In Australian Dollars", default="0")
    before_tax = models.CharField(_("Total Before Tax"), max_length=50, help_text="In Australian Dollars", default="0")
    coupon = models.ForeignKey(OrderCoupon, verbose_name=_("Coupon applied"), on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(_("Cooking Instructions"), max_length=255, blank=True, null=True)
    
    def __str__(self)-> str:
        return f"{self.user}"
    
    class Meta:
        ordering = ["-order_time"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        if not self.order_id:
            if self.schedule_date:
                try:
                    schedule_dt = datetime.strptime(self.schedule_date, "%Y-%m-%d")
                    today_str = schedule_dt.strftime("%d%m%y")  # e.g. 180125 for 18/01/25
                except ValueError:
                    # Fallback if schedule_date doesn't parse properly
                    today_str = datetime.now().strftime("%d%m%y")
            else:
                # If no schedule_date is set, fall back to today's date
                today_str = datetime.now().strftime("%d%m%y")

            prefix = f"CHDS{today_str}"

            # Find the latest order matching our prefix
            last_order = Orders.objects.filter(
                order_id__startswith=prefix
            ).order_by("-order_id").first()

            if last_order:
                # Parse out the last 4 digits as an integer
                last_sequence_num = int(last_order.order_id[-4:])
                next_sequence_num = last_sequence_num + 1
            else:
                next_sequence_num = 1

            # Format the sequence number with leading zeros
            self.order_id = f"{prefix}{next_sequence_num:04d}"

        super().save(*args, **kwargs)
