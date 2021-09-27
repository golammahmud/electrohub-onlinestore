from django.conf import settings
from django.shortcuts import render, redirect
#
# from cart.models import Cart

def cart_detail(request):
    return render(request, template_name='cart.html', )

