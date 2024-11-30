from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.orders.models import Orders
from apps.orders.email import NotifyUserViaMail

@receiver(post_save,sender = Orders)
def NotifyUser(sender,instance,created,**kwargs):
    if created:...
    else:
        customer_name = instance.user.full_name
        if not customer_name:
            customer_name="Customer"
        if instance.status == "Order Placed":
            subject="Your Order is Confirmed!"
            message =f"""
            Hi {customer_name},
            Thank you for your order.
            We're excited to let you know that your order has been placed """
        elif instance.status == "Payment Success":
            subject="Your Payment is Confirmed!"
            message =f"""
            Hi {customer_name}
            Thank you for your order.
            Your payment for order number {instance.order_id} has been successfully processed.
            """
        elif instance.status == "Payment Failed":
            subject=f"Payment Failed for Order id {instance.order_id}"
            message =f"""
            Hi {customer_name},
            Unfortunately, your payment for order number {instance.order_id} has failed..
             """
        elif instance.status == "Ready for Pickup":
            subject="Your Order is Ready for Pickup!"
            message =f"""
            Hi {customer_name},
            Your order is now ready for pickup.
            """
        elif instance.status == "Out for Delivery":
            subject="Your Order is Out for Delivery!"
            message =f"""
            Hi {customer_name},
            Your order is on its way!
            """
        elif instance.status == "Delivered":
            subject="Your Order Has Been Delivered!"
            message =f"""
            Hi {customer_name},
            Your order has been successfully delivered.
            Thank you for choosing us.
            """
        elif instance.status == "Cancelled":
            subject="Your Order Has Been Cancelled"
            message =f"""
            Hi {customer_name},
            We regret to inform you that your order number {instance.order_id} has been cancelled."""
       
        NotifyUserViaMail(
            subject=subject,
            message=message,
            recipient_list=[instance.user.email]
        )
        
    
    
