from rest_framework import serializers
from apps.orders.models import Orders
from apps.transactions.models import Transaction


class OrderSerializer(serializers.ModelSerializer):
    delivery_location = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    pickup_location = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    notes = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    menu_item = serializers.JSONField()

    class Meta:
        model = Orders
        fields = ["pickup_location", "schedule_date", "time_slot", "order_type", "delivery_location", "amount", "menu_item","shipping_charges","total_price", "notes"]
        
        
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
    order_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Orders
        fields ="__all__"
        
    def get_transaction(self,obj):
        data = obj.transaction
        return ListTransactionSerilaizer(data).data
    
    def get_order_time(self, obj):
        if obj.order_time:
            return obj.order_time.strftime("%Y-%m-%d %H:%M:%S")
        return None