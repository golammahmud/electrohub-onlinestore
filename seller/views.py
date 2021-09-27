from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
from django.core.exceptions import ValidationError
from users.forms import  RegistrationFormSeller, RegistrationFormSeller2,CustomAuthenticationForm
from django.urls import reverse_lazy, reverse
from users.models import SellerAdditional, CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# from firstproject import settings
from django.core.mail import EmailMessage
# from .tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from  shop.models import  Product,ProductImage,ProductFeatures,ProductFacility
# Create your views here.

from .forms import SellerProduct,ProductFacilityForm,ProductFeaturesForm,ProductImageForm

from django.urls import reverse_lazy


from users.forms import SellerAuthenticationForm,sellerPictureForm,SellerProfileUpdateFrom
from users.models import Seller,CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from order.models import Order,OrderItem
from datetime import datetime
from order.forms import OrderUpdateForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 

def prodect_details(request,category_slug,slug):
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
    return render(request,template_name='product_details.html',context={'facility':facility,'product':product,'photos':photos,'feature':feature})



def SellerRegistrationView(request):
    form = RegistrationFormSeller(request.POST,None)
    if form.is_valid():
        user = form.save()
        if user.is_seller:
            
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("seller_profile")
            
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=RegistrationFormSeller()
    return render (request, template_name="signup.html", context={"form":form})
    

def SellerLogin(request):
    if request.user.is_authenticated and  request.user.is_seller is True:
        messages.info(request, message='you are already logged in')
        return redirect('seller_profile')
    else:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                remember_me = form.cleaned_data['remember_me']
                user = authenticate(username=username, password=password)
                print(user.type)
                if user.Types.SELLER:
                    if user is not None: 
                        request.session['seller'] = user.id
                        if user.is_seller is True:
                            
                            login(request, user)
                        
                            if remember_me:
                                request.session.set_expiry(1209600)
                            messages.info(request, f"You are now logged in as {username}")
                            return redirect('seller_profile')
                        else:
                             messages.error(request, "Invalid username or password.")
                    else:
                        messages.error(request, "Invalid username or password.")
           
            else:
                messages.error(request, "Invalid username or password.")
        form = CustomAuthenticationForm()
        
    return render(request, template_name='signin.html' ,context={'form':form })



class sellerProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'seller_profile.html')
    
        # return render(request, 'seller_profile.html')
        

# class OrderStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Order
#     template_name = 'order_status_update.html'
#     form_class=OrderUpdateForm
#     context_object_name ='order'
    

#     def form_valid(self, form):
#         form.instance.vendor = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.suplier:
#             return True
#         return False

def AllOrder(request):
    orders=Order.objects.all().order_by('-id')
    orderitem=OrderItem.get_orderitem_by_seller(orders)
    
    return render(request, template_name='allorders.html', context={'orders':orders,'orderitem':orderitem })

def  OrderStatusUpdateView(request ,id):
   
        order=get_object_or_404(Order,id=id)
        form=OrderUpdateForm(request.POST,instance=order)
        
        if form.is_valid():
            form.save()
            return redirect('product_order')
        else:
             form=OrderUpdateForm(instance=order)
             
        return render(request,template_name='order_status_update.html', context={'form':form})
        
       

def OrderView(request):
    try:
        vendor = request.user
        products = vendor.products.all()
        orders = Order.get_orders_by_seller(vendor)
    
        print(orders)
    
        orderitem=OrderItem.get_orderitem_by_seller(orders)
    except Exception as e:
        messages.info(request, message={e})
    # orderitem=get_object_or_404(OrderItem, order__in=orders)
    # print(orderitem)
 
    # for product in orderitem:
    #     p=product.product.name
    #     print(p)
   
    
    # print(orderitem)
   
 
    # orderitem=OrderItem.get_orderitem_by_seller(orders)
    # orderitem=OrderItem.get_orderitem_by_seller(orders)
    return render(request, template_name='orders.html', context= {  'orderitem':orderitem, 'orders':orders,'vendor':vendor,'products':products })
    
    
def Seller_Product(request):
    vendor = request.user
   
    products = vendor.products.all()
    

   

    return render(request, 'seller/seller_product.html', {'vendor': vendor, 'products': products})

def ProfilePictureUpdate(request):
    if request.method == "POST":
        # u_form=CustomerUpdateForm(request.POST,instance=request.user)
        p_form=sellerPictureForm(request.POST,request.FILES,instance=request.user)
        
        if  p_form.is_valid():
            p_form.save()
            messages.success(request,'your profile picture have been updated')
            return redirect('seller_profile')
    else:
        # u_form=CustomerUpdateForm(instance=request.user)
        p_form=sellerPictureForm(instance=request.user)
        
    return render(request,template_name='seller_picture_update.html',context = {'p_form':p_form})

def UpdateSellerProfile(request):
    if request.method == "POST":
        u_form=SellerProfileUpdateFrom(request.POST,instance=request.user)
        p_form=sellerPictureForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request,'you have been updated')
            return redirect('seller_profile')
    else:
        u_form=SellerProfileUpdateFrom(instance=request.user)
        # p_form=CustomerPictureForm(instance=request.user)
        
    return render(request,template_name='seller_update_profile.html',context = {'u_form':u_form})   


def SellerView(request):
    return render(request,'seller.html')


def logout_request(request):
   
    logout(request)
    messages.info(request, "You have been successfully logged out ") 
  #  return redirect("seller")



class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class=SellerProduct
    success_url = '/profile/'
    # fields = ['title', 'slug', 'content', 'p_image','category',]

    def form_valid(self, form):
        form.instance.suplier = self.request.user
        return super().form_valid(form)




# def CreateSellerProduct(request):
#     if request.method == "post":
#         form=SellerProduct(request.POST ,None)
#         facility=ProductFacility(request.POST ,None)
#         feature=ProductFeatures(request.POST ,None)
#         images=ProductImage(request.POST ,None)
       
        
#         if form.is_valid() and facility.is_valid() and feature.is_valid() and images.is_valid():
            
          
#             if form.instance.suplier==request.user:
#                 suplier=form.instance.suplier
#                 print(suplier)
            
#                 print(form.instance.suplier)
#                 form.save(commit=True)
#                 facility.save()
#                 feature.save()
#                 images.save()
#                 messages.success(request, message='succefully added your product')
#                 return redirect('seller_profile')
#             else:
#                 messages.warning(request, message='product added failed .something wrong ....please try again properly.....!')
#         else:
#             messages.warning(request, message='product add failed .please try again properly.....!')
            
#     else:
#         form=SellerProduct()
#         facility=ProductFacility()
#         feature=ProductFeatures()
#         images=ProductImage()
        
#     return render(request,template_name='create_product.html', context={'form':form,'facility':facility,'feature':feature,'images':images})


class CreateSellerProductView(TemplateView):
    product_form_class=SellerProduct
    facility_form_class=ProductFacility
    feature_form_class=ProductFeatures
    images_form_class=ProductImage
       
    # post_form_class = AddPostForm
    # comment_form_class = AddCommentForm
    template_name = 'create_product.html'

   
  
    def post(self, request):
        post_data = request.POST or None
        product_form=self.product_form_class(post_data,prefix='product')
        facility_form=self.facility_form_class(post_data,prefix='facility')
        feature_form=self.feature_form_class(post_data,prefix='feature')
        images_form=self.images_form_class(post_data,prefix='images')
        # post_form = self.post_form_class(post_data, prefix='post')
        # comment_form = self.comment_form_class(post_data, prefix='comment')

        context = self.get_context_data(product_form=product_form,
                                        facility_form=facility_form,
                                        feature_form=feature_form,
                                        images_form=images_form)

        if product_form.is_valid():
            # self.form_save(product_form)
            self.product.save(commit=True)
        if facility_form.is_valid():
            # self.form_save(facility_form)
            self.facility.save()
        if feature_form.is_valid():
            # self.form_save(feature_form)
            self.feature.save()
        if images_form.is_valid():
            # self.form_save(images_form)
            self.images.save()
        
        return self.render_to_response(context)  
 
    # def form_save(self, form):
    #     obj = form.save()
    #     messages.success(self.request, "{} saved successfully".format(obj))
    #     return obj
    def form_valid(self, form):
        form.instance.suplier = self.request.user
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    
def CreateSellerProduct(request):
    if request.method == 'POST':
        form = SellerProduct(request.POST, request.FILES)
       
        if form.is_valid() :
            form.save(commit=False)
            form.instance.suplier = request.user
            # if form.approve is True:
            # product.slug = slugify(product.title)
            
            form.save()
         
           
            # feature.save()
            # images.save()

            return redirect('seller_profile')
    else:
        form = SellerProduct()
      
    return render(request,template_name='add_product.html',context= {'form': form})


def Add_image_feature_Product(request,slug):
    seller=request.user
    product=seller.products.get(slug=slug)
    # facility=ProductFacility.objects.filter(product=product)
    # feature=ProductFeatures.objects.filter(product=product)
    # images=ProductImage.objects.filter(product=product)
    print(product)
    if request.method == 'POST':
        form = SellerProduct(request.POST, request.FILES, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        facility=ProductFacilityForm(request.POST )
        feature=ProductFeaturesForm(request.POST )
        if image_form.is_valid() and form.is_valid() and facility.is_valid() and feature.is_valid():
                    productimage = image_form.save(commit=False)
                    productimage.product = product
                    productimage.save()
                    
                    
                    facility=facility.save(commit=False)
                    facility.product= product
                    facility.save()
                    feature=feature.save(commit=False)
                    feature.product= product
                    feature.save()
                    form.save()
                    messages.success(request, message='product update successfully')
                    return redirect('seller_Product')

        else:
            messages.error(request, message='form is not valid!')
            

    else:
        form = SellerProduct(instance=product)
        facility=ProductFacilityForm()
        feature=ProductFeaturesForm( )
        image_form = ProductImageForm( )
    return render(request, template_name='add_img_feature.html', context={'form':form,'image_form':image_form, 'product': product,'facility':facility,'feature':feature})
def Edit_Product(request,slug):
    seller=request.user
    product=seller.products.get(slug=slug)
 
   
    facility=product.product_facility.get(product=product)
    feature=product.product_feature.get(product=product)
    images=product.product_images.get(product=product)
    print(product)
    if request.method == 'POST':
        form = SellerProduct(request.POST, request.FILES, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES , instance=images)
        facility=ProductFacilityForm(request.POST , instance=facility)
        feature=ProductFeaturesForm(request.POST, instance=feature )
        if  form.is_valid() and facility.is_valid() :
                    productimage = image_form.save(commit=False)
                    productimage.product = product
                    productimage.save()
                    
                    
                    facility=facility.save(commit=False)
                    facility.product= product
                    facility.save()
                    feature=feature.save(commit=False)
                    feature.product= product
                    feature.save()
                    form.save()
                    messages.success(request, message='product update successfully')
                    return redirect('seller_Product')

        else:
            messages.error(request, message='form is not valid!')
            

    else:
        form = SellerProduct(instance=product)
        facility=ProductFacilityForm(instance=facility)
        feature=ProductFeaturesForm( instance=feature)
        image_form = ProductImageForm( instance=images)
    return render(request, template_name='edit_product.html', context={'form':form,'product': product,'facility':facility,'feature':feature,'image_form':image_form})

class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'edit_product.html'
    form_class=SellerProduct
    

    def form_valid(self, form):
        form.instance.sulier = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.suplier:
            return True
        return False
    
class DeleteProduct(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy("seller_Product")

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.suplier:
            return True
        return False