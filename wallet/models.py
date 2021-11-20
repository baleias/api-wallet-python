from django.db import models
from cpf_field.models import CPFField

class Customer(models.Model):
    name = models.CharField(max_length=100)
    cpf = CPFField('cpf')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPES =[
        ('A', 'Produto A'),
        ('B', 'Produto B'),
        ('C', 'Produto C'),
    ]

    types = models.CharField(
        max_length=1,
        choices=PRODUCT_TYPES,
        default='A'
    )
    product_name = models.CharField(max_length=20, default='name of the product')
    value = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.product_name

class OrderItem(models.Model):
    products = models.ManyToManyField('Product')
    qty = models.IntegerField(default=1)
    def get_total_products(self):
        total_items = 0
        for product in self.products.all():
            total_items += product.value
        total_items *= self.qty
        return total_items

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, default=" ")
    order_items = models.ManyToManyField('OrderItem')
    def get_total_order(self):
        total_order = 0
        for order_item in self.order_items.all():
            total_order += order_item.get_total_products()
        return total_order

    def __str__(self):
        return self.customer.name

class Cashback(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    sold_date = models.DateTimeField(auto_now=True)
    total = models.IntegerField(null=True, blank=True)

    def get_cashback(self):
        total_order = self.order.get_total_order()
        if (total_order <= 100): #When the order is 100 or less, cashback is 7%#
            cashback = total_order * 0.07
            return cashback
        elif (total_order <=200): #When the order is up to 200, cashback is 10%#
            cashback = total_order * 0.10
            return cashback
        else: #When Order is more than 200, cashback is 12%#
            cashback = total_order * 0.12
            return cashback
        
        

    

