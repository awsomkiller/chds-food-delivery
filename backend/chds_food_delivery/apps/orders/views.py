from rest_framework.viewsets import ModelViewSet
from apps.orders.serializers import OrderSerializer
from apps.orders.models import Orders

class OrdersApi(ModelViewSet):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Orders.objects.all().filter(user=self.request.user)
    