from apps.restaurants.models import MenuPortionPriceList, Addons, PickupLocation, DeliveryPoint
from apps.users.models import UserAddress

import json

def process_menu_item_cost(item):
    portion_id = item.get('selected_meal_portion_id', None)
    pricelist = MenuPortionPriceList.objects.get(id=portion_id)
    item_price = pricelist.price
    addon_price = fetch_addons_price(item.get('addons', []))
    return (int(item_price) + int(addon_price)) * int(item.get('quantity'))

def fetch_addons_price(addons):
    addon_price = 0
    for addon in addons:
        id = addon.get('id')
        instance = Addons.objects.get(id = id)
        addon_price += int(instance.price)
    return addon_price

def get_shipping_charge(data):
    if data['order_type'] == "PICKUP":
        # pickup_location  = data.get("pickup_location")
        # pickup_instance = PickupLocation.objects.get(id=pickup_location)
        # if not pickup_instance:
        #     raise "Pickup location Not Found"
        # shipping_charges = pickup_instance.price
        # return shipping_charges
        return '0'
           
    elif data['order_type'] == "DELIVERY":
        delivery_location = data.get("delivery_location")
        delivery_instance = UserAddress.objects.get(id=delivery_location)
        pincode_instance = DeliveryPoint.objects.filter(postal_code=delivery_instance.postal_code).first()
        shipping_charges = pincode_instance.price 
        return shipping_charges
    else:
        raise "Unknown Order Type"

def calculate_discount(data, coupon):
    amount = data.get('amount')
    menu_item = json.loads(data.get('menu_item'))
    discount = 0
    if coupon.discount_type == "PERCENTAGE":
        amount = data.get('amount')
        discount = (coupon.discount_upto * amount) / 100
    elif coupon.discount_type == "FIXED_ORDER":
        amount = data.get('amount')
        discount = (coupon.discount_upto * amount) / 100
    else:
        for item in menu_item:
            discount += calculate_discount_per_item(coupon, item.get('quantity'))
    return discount
        
def calculate_discount_per_item(coupon, quantity):
        return coupon.discount_upto * quantity