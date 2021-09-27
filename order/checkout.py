from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from users.models import Customer
from django.views import View

from shop.models import Product
from order.models import Order,OrderItem
from django.contrib import messages
from order.forms import OrderForm
from shop.views import Cart


def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], vendor=item['product'].vendor, price=item['product'].price, quantity=item['quantity'])
    
        order.vendors.add(item['product'].vendor)

    return order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        recived_area = request.POST.get('recived_area')
        print(recived_area)
        phone = request.POST.get('phone')
        cash_on_payment= request.GET.get('cash_on')
        print(f'cash on delivery:{cash_on_payment}')
        # customer = request.session.get('customer')
        # print(customer)
        customer = request.user.id
        customer=Customer(id=customer)
        print(f'the customer name:{customer.name}')
        cart = request.session.get('cart')
       
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer.name, cart, products)
        if products !='' and cart!='':
            for product in products:
                print(cart.get(str(product.id)))
                order = Order(customer=customer,
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            order_area=recived_area,
                            quantity=cart.get(str(product.id)),
                            payment_status=cash_on_payment,
                            
                            )         
                order.save()
                orderitem=OrderItem(order=order, product=product, vendor=product.suplier, price=product.price, quantity=cart.get(str(product.id)))
                orderitem.save()
                messages.success(request,message='succefully placed your order...please stay with us for this delivery')
            request.session['cart'] = {}
            
            return redirect('cart')
        
        else:
            messages.warning(request, message='you are not add cart any product!')
            
