from django.contrib import admin
from .models import Customer, OrderItem, Product, Order, Cashback

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cashback)
