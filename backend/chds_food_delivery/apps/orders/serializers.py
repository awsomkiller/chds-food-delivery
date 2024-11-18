from rest_framework import serializers
from apps.orders.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["restaurant_id","user","order_time","delivery_time","status","amount","transaction","menu_item"]