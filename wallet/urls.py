from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view(), name='Customer'),
    path('product/', views.OrderList.as_view(), name='Order'),
    path('cashback/', views.CashbackList.as_view(), name='Cashback'),
]