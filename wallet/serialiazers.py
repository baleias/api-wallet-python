from .models import Customer, Order, Cashback
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = '__all__'