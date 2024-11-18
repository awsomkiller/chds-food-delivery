from django.db import models
from apps.restaurants.models import Restaurant
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.transactions.models import Transaction

class Orders(models.Model):
    ORDER_STATUS=[
        ('ORDER_PREPARING','Order Preparing'),
        ('PACKED', 'Packed'),
        ('READY_FOR_PICKUP', 'Ready for Pickup'),
        ('SHIPPED', 'Shipped'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
        
    ]
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING, related_name="orders")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="userorders")
    order_time = models.DateTimeField(_("Order Time"))
    delivery_time = models.DateTimeField(_("Delivery Time"))
    status = models.CharField(max_length=20,choices=ORDER_STATUS)
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    menu_item = models.JSONField(_("Menu Items"),help_text="Selected Menu items Json object")
    
    
    def __str__(self)-> str:
        return f"{self.user}-{self.restaurant_id.name}"
    
    class Meta:
        ordering = ["-order_time"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"