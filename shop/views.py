from django.shortcuts import render,get_object_or_404

from shop.models import MyShop,Subcategory,Product,ProductImage,Orders,Banar,Banar_carnival,ProductFeatures,Newsletter,ProductFacility
# from shop.forms import CustomerForm,OnlineShopForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.db.models import Q
from datetime import datetime

import speech_recognition as sr
import pyttsx3
from django.views import View
from users.models import Customer

from order.models import Order
from order.forms import OrderForm

def talk(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening.....')
            talk('listening.....')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = ''
            try:
                print("Recognizing...")
                talk("Recognizing...")
                command = listener.recognize_google(voice, language='en-in')
                command = command.lower()
                # command=''
                # if 'romeo' in command:
                #     command = command.replace('romeo', '')
                #     print(command)
                # else:
                #     pass
                # return command
            except:
                pass
                talk('Unable to Recognize your voice.')
            return command

    except Exception as e:
        print(e)
# def contact(request):
    
#     return render(request, template_name='shop/contact.html')

def newsletter(request):
    if request.method=='POST':
        email = request.POST.get('email')
        print(email)
        if email!='':
            nemail=Newsletter.objects.create(email=email)
            nemail.save()
            messages.success(request, message='your email saved succefully ')
            return redirect('home')
        else:
            messages.warning(request,'email address required for subscription')
            
# -----------------------------cart-------------------------

def MakePayment( request):
    return render(request , 'shop/payment2.html' )

    
class Cart(View):
    def post(self, request):
        form=OrderForm(request.POST)
        try:
            product = request.POST.get('product')
            print(f'the product id is:{product}')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product]  = quantity-1
                    else:
                        cart[product]  = quantity+1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart' , request.session['cart'])
            return redirect('cart')
        except :
            messages.warning(request,'there is something wrong!')
        
        return render(request , 'shop/cart.html' , {'form':form ,'remove':remove} )

    def get(self , request):
        # try:
        products = ''
        customer = ''
           
        ids = list(request.session.get('cart').keys())
        print(ids)
        if ids is not None:
            
            products = Product.get_products_by_id(ids)
            customer = Customer.objects.filter(name=request.session.get('cart'))
            print(customer)
            print(products)
        else:
            messages.warning(request,message='you are not add cart any products!')
        #orders
        customer = request.session.get('customer')
        # print(customer)
        orders = Order.get_orders_by_customer(customer)
        # print(orders)
        # except :
        #     messages.warning(request, message='please first add cart products!')
        return render(request , 'shop/cart.html' , {'products' : products,'customer':customer ,'orders':orders } )

# -----------------------------product cart-------------------------
class index(View):
    def post(self , request):
        try:
            product = request.POST.get('product')
            print(f'the product id is:{product}')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product]  = quantity-1
                    else:
                        cart[product]  = quantity+1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart' , request.session['cart'])
            return redirect('home')
        except :
            messages.warning(request,'there is something wrong!')
    
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products=Product.objects.filter(is_featured=True,is_approved=True)
        category=Subcategory.objects.filter(parent=None)[:12]
        featured_category=Subcategory.objects.filter(is_featured=True).order_by('pk')
        popular_products = Product.objects.filter(is_approved=True).order_by('-num_visits')[0:4]
        recently_viewed_products = Product.objects.filter(is_approved=True).order_by('-last_visit')[0:4]
        
        
        banar=Banar.objects.all()
        carnival=Banar_carnival.objects.all()
        return render(request,template_name='shop/index2.html',context={'category':category,
                                                                        'featured_category':featured_category,
                                                                        'products': products,
                                                                        'popular_products': popular_products,
                                                                    'recently_viewed_products': recently_viewed_products})
        # return render(request,template_name='shop/index2.html',context={'category':category,'featured_products':featured_products,
    #                                                                "featured_category":featured_category,'banar':banar
    #                                                                ,'carnival':carnival})



def prodect_details(request,category_slug,slug):
    if request.method=='POST':
        try:
            product = request.POST.get('product')
            print(f'the product id is:{product}')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product]  = quantity-1
                    else:
                        cart[product]  = quantity+1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart' , request.session['cart'])
            return redirect('product_details')
        except :
            messages.warning(request,'there is something wrong!')
        
    product=get_object_or_404(Product,slug=slug ,is_approved=True)
    photos=ProductImage.objects.filter(product=product)
    feature=ProductFeatures.objects.filter(product=product)
    facility=ProductFacility.objects.filter(product=product)
    product.num_visits=product.num_visits+1
    product.last_visit=datetime.now()
    product.save()
    
    if product.parent:
        return redirect('product_details', category_slug=category_slug, slug=product.variasions.slug)

    
    # return render(request,template_name='shop/product_details.html',context={'product':product,'photos':photos})
    return render(request,template_name='shop/myprod.html',context={'facility':facility,'product':product,'photos':photos,'feature':feature})




def Category_details(request,category_slug):
    # category=get_object_or_404(Subcategory,slug=category_slug).order_by('-pk')
    # #cat_children=Subcategory.children.filter(parent=None)
    # return render(request,template_name='shop/category_details.html',context={'category':category})#,'cat_children':cat_children

    if request.method=='POST':
        try:
            product = request.POST.get('product')
            print(f'the product id is:{product}')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product]  = quantity-1
                    else:
                        cart[product]  = quantity+1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart' , request.session['cart'])
            return redirect('product_details')
        except :
            messages.warning(request,'there is something wrong!')
    
    category = get_object_or_404(Subcategory, slug=category_slug)
    products = category.products.filter(parent=None,is_approved=True)
    
   
    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'shop/category_details.html', context)

def product_category(request):
    category=Subcategory.objects.all()
    # #main_categories=Subcategory.objects.filter(parent=None)
    # main_categories=Subcategory.objects.all()
    # main_1st=main_categories[0:3]

    return render(request,template_name='shop/product_categories.html', context={'category':category})

def product_category(request):
    category=Subcategory.objects.all()
    # #main_categories=Subcategory.objects.filter(parent=None)
    # main_categories=Subcategory.objects.all()
    # main_1st=main_categories[0:3]

    return render(request,template_name='shop/product_categories.html', context={'category':category})

def All_Products(request):
    if request.method=='POST':
        try:
            product = request.POST.get('product')
            print(f'the product id is:{product}')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product]  = quantity-1
                    else:
                        cart[product]  = quantity+1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart' , request.session['cart'])
            return redirect('product_details')
        except :
            messages.warning(request,'there is something wrong!')
    
    
    products=Product.objects.all(is_approved=True).order_by('-pk')
    
    return render(request,template_name='shop/product.html', context ={'products':products})


def about(request):
    return render(request,template_name='shop/about.html')
def search(request):
    
    
    # query = request.GET.get('query')


    query = request.GET.get('query')[:50]
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_created')
    category=Subcategory.objects.filter(name__icontains=query)
   
    if len(query) > 100:
        product = Product.objects.none()
    elif len(query) < 1:
        product = Product.objects.none()
        messages.warning(request, 'no search results found..please try again proper query')

    # if product.count()==0:
    #     messages.warning(request,'no search results found..please try again proper query')

    else:
    
        product= Product.objects.filter(Q(category__in=category) | Q(name__icontains=query) | Q(price__icontains=query)
                                   | Q(description__icontains=query) | Q(date_created__date__icontains=query))
        if instock:
            product = product.filter(stock__gte=1)
        elif price_from and price_to :
            product = product.filter(price__gte=price_from).filter(price__lte=price_to)
            
    context = {
        'query': query,
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting,
        'product':product.order_by(sorting),
    }
    
    return render(request, 'shop/search2.html', context)


def voice_search(request):
    
    query =take_command()
    print( query )
    talk(query)
    # instock = request.GET.get('instock')
    # price_from = request.GET.get('price_from', 0)
    # price_to = request.GET.get('price_to', 100000)
    # sorting = request.GET.get('sorting', '-date_created')
    category = Subcategory.objects.filter(name__icontains=query)


    product = Product.objects.filter(Q(category__in=category) | Q(name__icontains=query) | Q(price__icontains=query)
                                     | Q(description__icontains=query) | Q(date_created__date__icontains=query))


    context = {
        'query': query,
        # 'instock': instock,
        # 'price_from': price_from,
        # 'price_to': price_to,
        # 'sorting': sorting,
        # 'product': product.order_by(sorting),
        'product':product
    }

    # ------------------------------------------voice----------------------------------------
    # query = request.GET.get('query')
    # instock = request.GET.get('instock')
    # price_from = request.GET.get('price_from', 0)
    # price_to = request.GET.get('price_to', 100000)
    # sorting = request.GET.get('sorting', '-date_added')
    # products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)

    # if instock:
    #     products = products.filter(num_available__gte=1)

    # query = request.GET.get('query')[:50]
    # category=Subcategory.objects.filter(Q(name__icontains=query))
    
    # if len(query) > 100:
    #     product = Product.objects.none()
    # elif len(query) < 1:
    #     product = Product.objects.none()
    #     messages.warning(request, 'no search results found..please try again proper query')

    # # if post.count()==0:
    # #     messages.warning(request,'no search results found..please try again proper query')
    # else:
    #     product= Product.objects.filter(Q(category__in=category) | Q(name__icontains=query) | Q(price__icontains=query)
    #                                | Q(description__icontains=query) | Q(date_created__date__icontains=query))
    # context = {
    #     'query': query,
    #     'product':product
    #     # 'products': products.order_by(sorting),
    #     # 'instock': instock,
    #     # 'price_from': price_from,
    #     # 'price_to': price_to,
    #     # 'sorting': sorting
    # }

    return render(request, 'shop/search2.html')

def checkout(request):
    return render(request,template_name='shop/checkout.html' )