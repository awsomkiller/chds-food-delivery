from django.db import models
from apps.restaurants.models import PickupLocation,WorkingDays
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.transactions.models import Transaction
import uuid

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
    
    def __str__(self)-> str:
        return f"{self.user}"
    
    class Meta:
        ordering = ["-order_time"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())
        super().save(*args, **kwargs)
        
