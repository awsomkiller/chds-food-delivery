from rest_framework import serializers
from apps.orders.models import Orders
from apps.transactions.models import Transaction


class OrderSerializer(serializers.ModelSerializer):
    delivery_location = serializers.CharField(required=False)
    pickup_location = serializers.CharField(required=False)
    menu_item = serializers.JSONField()

    class Meta:
        model = Orders
        fields = ["pickup_location", "schedule_date", "time_slot", "order_type", "delivery_location", "amount", "menu_item","shipping_charges","total_price"]
        
        
    def create(self, validated_data):
        # Get the user from context
        request = self.context.get('request')
        user = request.user if request else None

        # Create the instance, assigning the user to the 'user' field
        instance = Orders.objects.create(user=user, **validated_data)

        return instance
   
class ListTransactionSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields ="__all__" 
        
class ListOrdersSerilaizer(serializers.ModelSerializer):
    transaction=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Orders
        fields ="__all__"
        
    def get_transaction(self,obj):
        data = obj.transaction
        return ListTransactionSerilaizer(data).data