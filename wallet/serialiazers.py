from .models import Customer, Order, Cashback
from rest_framework import serializers
from wallet.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def validate(self, data):
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf' : "CPF is invalid"})
        return data
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = '__all__'