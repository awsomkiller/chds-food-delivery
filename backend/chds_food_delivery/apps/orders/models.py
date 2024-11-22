from django.db import models
from apps.restaurants.models import PickupLocation,TimeSlots
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.transactions.models import Transaction

class Orders(models.Model):
    ORDER_STATUS=[
        ("ORDER_PLACED","Order Placed"),
        ('ORDER_PREPARING','Order Preparing'),
        ('PACKED', 'Packed'),
        ('READY_FOR_PICKUP', 'Ready for Pickup'),
        ('SHIPPED', 'Shipped'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
        
    ]
    ORDER_TYPES =[
        ("PICKUP","Pickup"),
        ("DELIVERY","Delivery")
    ]
    pickup_location = models.ForeignKey(PickupLocation,on_delete=models.DO_NOTHING, related_name="orders",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="userorders")
    order_time = models.DateTimeField(_("Order Time"))
    delivery_date= models.DateField(_("Delivery Date"),null=True)
    time_slots = models.ForeignKey(TimeSlots,on_delete=models.DO_NOTHING,related_name="time_slots",null=True)
    order_type = models.CharField(_("Order Type"),choices=ORDER_TYPES,max_length=10,null=True)
    delivery_location = models.TextField(_("Delivery Location"),default="NA")
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default="ORDER_PLACED")
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    menu_item = models.JSONField(_("Menu Items"),help_text="Selected Menu items Json object")
    
    
    def __str__(self)-> str:
        return f"{self.user}-{self.pickup_location.name}"
    
    class Meta:
        ordering = ["-order_time"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        
