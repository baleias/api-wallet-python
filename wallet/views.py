from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from wallet.models import Customer, Order, Cashback
from wallet.serialiazers import CustomerSerializer, OrderSerializer, CashbackSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CashbackList(generics.ListCreateAPIView):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer