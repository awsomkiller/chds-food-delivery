from rest_framework import serializers
from apps.transactions.models import Transaction,WalletCoupon, OrderCoupon

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class WalletCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletCoupon
        fields = '__all__'

class OrderCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCoupon
        fields = '__all__'
