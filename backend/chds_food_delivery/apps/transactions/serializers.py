from rest_framework import serializers
from decimal import Decimal
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


class WalletRechargeSerializer(serializers.Serializer):
    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=Decimal(1.00),
        help_text="Amount to recharge the wallet."
    )
    payment_method_id = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        help_text="Stripe payment method ID."
    )

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid Recharge amount")
        return value
