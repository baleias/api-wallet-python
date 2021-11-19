from django.db import models
from django.db.models.fields import CharField, IntegerField, DecimalField, DateTimeField
from cpf_field.models import CPFField

class Customer(models.Model):
    name = models.CharField(max_length=100)
    cpf = CPFField('cpf')

class Product(models.Model):
    PRODUCT_TYPES =[
        ('A', 'Produto A'),
        ('B', 'Produto B'),
        ('C', 'Produto C'),
    ]

    types = models.CharField(
        max_length=2,
        choices=PRODUCT_TYPES,
        default='A'
    )

    value = models.DecimalField(max_digits=8, decimal_places=2)

class Order_Item(models.Model):
    qty = models.IntegerField(max_length=2, default=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    ordem_item = models.ManyToManyField('Order_Item')
    

class Cashback(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    sold_date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(null=True, blank=True)

    

