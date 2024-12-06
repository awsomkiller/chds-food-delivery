from apps.restaurants.models import MenuPortionPriceList, Addons, PickupLocation, DeliveryPoint
from apps.users.models import UserAddress

def process_menu_item_cost(item):
    portion_id = item.get('selected_meal_portion_id', None)
    pricelist = MenuPortionPriceList.objects.get(id=portion_id)
    item_price = pricelist.price
    addon_price = fetch_addons_price(item.get('addons', []))
    return int(item_price)+int(addon_price)

def fetch_addons_price(addons):
    addon_price = 0
    for addon in addons:
        id = addon.get('id')
        instance = Addons.objects.get(id = id)
        addon_price += int(instance.price)
    return addon_price

def get_shipping_charge(data):
    if data['order_type'] == "PICKUP":
        pickup_location  = data.get("pickup_location")
        pickup_instance = PickupLocation.objects.get(id=pickup_location)
        if not pickup_instance:
            raise "Pickup location Not Found"
        shipping_charges = pickup_instance.price
        return shipping_charges
           
    elif data['order_type'] == "DELIVERY":
        delivery_location = data.get("delivery_location")
        delivery_instance = UserAddress.objects.get(id=delivery_location)  
        if not delivery_instance:
            raise "Delivery location Not Found"
        pincode_instance = DeliveryPoint.objects.filter(postal_code=delivery_instance.postal_code).first()
        shipping_charges = pincode_instance.price 
        return shipping_charges
    else:
        raise "Unknown Order Type"