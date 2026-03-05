from rest_framework import viewsets
from .model import Payment
from api.Payment.serializer import PaymentSerializer
from rest_framework.permissions import AllowAny

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]