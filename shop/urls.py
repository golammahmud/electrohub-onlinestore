from django.contrib import admin
from django.urls import path,include
from .views import index,prodect_details,Category_details,product_category,All_Products,search,voice_search,about,checkout,newsletter,MakePayment
# from user.views import registrations,suplier_profile
# from user.views import login, seller_profile

 #user section------------------------------------------
from users.views import Login,logout_request,contact#SellerRegistrationView,CustomerProfileView,sellerProfileView,CustomerRegistrationView

 #user section------------------------------------------
from cart.views import cart_detail
from  order.middlewares.auth import  auth_middleware
from .views import Cart
from order.checkout import CheckOut
from order.views import OrderView,payment

urlpatterns = [
    path('',index.as_view(),name='home'),
    
    
    path('about/',about,name='about'),
    path('products/',All_Products ,name='all_products'),
    # path('user/registration/',registrations,name='registration'),
    path('product-category/',product_category,name='product_category'),
    path('search/', search, name='search'),
    path('voice-search/', voice_search, name='voice_search'),
    # path('suplier/',seller_profile,name='suplier_profile'),
    
    # path('product/checkout/',checkout, name='checkout'),
    
    #cart section
    path('payment/',MakePayment, name='payment'),
    path('newsletter/',newsletter , name='newsletter'),
    path('contact/',contact , name='contact'),
    path('cart/',auth_middleware(Cart.as_view()) , name='cart'),
    
    #end cart section
    #--------------order section------------
    path('check-out/', CheckOut.as_view() , name='checkout'),
    path('orders/', auth_middleware(OrderView.as_view()), name='order'),
  
    
    #user section------------------------------------------
    
    # path('seller/registration/',SellerRegistrationView, name='seller_registrations'),
    # path('customer/registration/',CustomerRegistrationView, name='customer_registrations'),
    path('login/', Login, name='login'),
    path('logout/', logout_request, name='logout'),
    # path('customer/profile/', CustomerProfileView.as_view(), name='customer_profile'),
    # path('seller/profile/', sellerProfileView.as_view(), name='seller_profile'),

     #user section------------------------------------------
    
    
    
    path('<slug:category_slug>/<slug:slug>/',prodect_details,name='product_details'),
    path('<slug:category_slug>/',Category_details,name='category_details'),
    
    
    
    
    
    # path('products/',Product,name='products'),
  
    #path('<slug:main_cat_slug>/<slug:sub_cat_slug>/',product_category,name='product_category'),

    # path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    
]
