from rest_framework import serializers
from apps.orders.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["pickup_location","user","order_time","delivery_date","time_slots","order_type","delivery_location","status","amount","transaction","menu_item"]