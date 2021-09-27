
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from users.models import Customer
from django.views import View

from shop.models import Product
from order.models import Order
from order.middlewares.auth import auth_middleware
from django.utils.decorators import  method_decorator

class OrderView(View):
    
    
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'order.html'  , {'orders' : orders})
    
def payment(request):
    
    return render(request ,template_name='payment.html')