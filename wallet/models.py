from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False)
    
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
        default='A', 
        blank=False
    )
    product_name = models.CharField(max_length=20, blank=False, null=False) 
    value = models.DecimalField(max_digits=8, decimal_places=2, blank=False)

    def __str__(self):
        return self.product_name

class OrderItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey('Order', related_name="items", on_delete=models.CASCADE)
    def get_total_products(self):
        total_items = 0
        for product in self.product.all():
            total_items += product.value
        total_items *= self.quantity
        return total_items

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    def get_total_order(self):
        total_order = 0
        for order_item in self.items.all():
            total_order += order_item.get_total_products()
        return total_order

    def __str__(self):
        return self.customer.name

class Cashback(models.Model):
    sold_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def get_cashback(self):
        total_order = self.order.get_total_order()
        cashback = 0
        if (total_order <= 100): #When the order is 100 or less, cashback is 7%#
            cashback = total_order * 7 / 100
        elif (total_order <=200): #When the order is up to 200, cashback is 10%#
            cashback = total_order * 10 / 100
        else: #When Order is more than 200, cashback is 12%#
            cashback = total_order * 12 / 100
        return cashback
        
    def save(self, *args, **kwargs):
        self.total = self.get_cashback()
        super().save(*args, **kwargs)
            
    def __str__(self):
        return str(self.total)

    

