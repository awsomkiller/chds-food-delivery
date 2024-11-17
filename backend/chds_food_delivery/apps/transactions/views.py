from rest_framework.viewsets import ModelViewSet
from apps.transactions.models import Transaction,WalletCoupon,OrderCoupon
from apps.transactions.serializers import TransactionSerializer ,WalletCouponSerializer,OrderCouponSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset =  self.queryset.filter(user=self.request.user)
        return queryset
    
    

class WalletCouponViewSet(ModelViewSet):
    queryset = WalletCoupon.objects.all()
    serializer_class = WalletCouponSerializer

    @action(detail=False, methods=['post'])
    def validate(self, request):
        code = request.data.get('code')
        try:
            coupon = WalletCoupon.objects.get(code=code)
            return Response({"valid": True, "coupon": WalletCouponSerializer(coupon).data})
        except WalletCoupon.DoesNotExist:
            return Response({"valid": False}, status=status.HTTP_404_NOT_FOUND)
        
        

class OrderCouponViewSet(ModelViewSet):
    queryset = OrderCoupon.objects.all()
    serializer_class = OrderCouponSerializer

    @action(detail=False, methods=['post'])
    def validate(self, request):
        code = request.data.get('code')
        try:
            coupon = OrderCoupon.objects.get(code=code)
            return Response({"valid": True, "coupon": OrderCouponSerializer(coupon).data})
        except OrderCoupon.DoesNotExist:
            return Response({"valid": False}, status=status.HTTP_404_NOT_FOUND)