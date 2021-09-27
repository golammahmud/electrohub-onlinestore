from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
from django.core.exceptions import ValidationError
from users.forms import  RegistrationFormSeller, RegistrationFormSeller2,RegistrationFormCustomer,CustomAuthenticationForm,CustomerAuthenticationForm,CustomerUpdateForm,ContactForm
from django.urls import reverse_lazy, reverse
from .models import SellerAdditional, CustomUser
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
from  shop.models import  MyShop
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['firstname']
        last_name = form.cleaned_data['lastname']
        name = first_name + '' + last_name
        email = form.cleaned_data['email']
        message = form.cleaned_data['msg']
        form.save()
        if name and message and email:
            subject = f'Message From  django Block of {first_name}'
            message = f'tthis message comes from {name}\n {message}\n {email}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['pranto.ahmed89@gmail.com']
            try:
                send_mail(subject,
                          message,
                          email_from,
                          recipient_list,
                          fail_silently=False)
                messages.success(request, f' Thanks {first_name} your message has been successfully sent!')
                return redirect('contact')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        # send_mail(
        #     subject,#subject
        #     message,#message
        #     email_from,#from email
        #     recipient_list,#to email

        #     fail_silently=False
        # )
        # messages.success(request,f' Thanks {first_name} your message has been successfully sent!')
        # return redirect('contact')
    else:

        form = ContactForm()
        myshop=MyShop.objects.all()
        # messages.warning(request,'please fill in all fields properly!')

    return render(request, 'contact.html', {'form': form ,'myshop':myshop})




# class SellerRegisterView(CreateView):
#     template_name = 'registerseller.html'
#     form_class = RegistrationFormSeller
#     success_url = reverse_lazy('home')
    
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 302:
#             gst = request.POST.get('gst')
#             warehouse_location = request.POST.get('warehouse_location')
#             user = CustomUser.objects.get(email = request.POST.get('email'))
#             s_add = SellerAdditional.objects.create(user = user, gst = gst, warehouse_location = warehouse_location)
#             return response
#         else:
#             return response

# -------------------------above done
    # def post(self, request, *args, **kwargs):
    #         #form = RegistrationForm(request.POST)
    #         user_email = request.POST.get('email')
    #         try:
    #             existing_user = CustomUser.objects.get(email = user_email)
    #             if(existing_user.is_active == False):
    #                 existing_user.delete()
    #         except:
    #             pass

# class CustomerRegisterView(CreateView):
#     template_name = 'registercustomer.html'
#     form_class = RegistrationFormCustomer
#     success_url = reverse_lazy('home')

#     def post(self, request, *args, **kwargs):
#             #form = RegistrationForm(request.POST)
#             user_email = request.POST.get('email')
#             try:
#                 existing_user = CustomUser.objects.get(email = user_email)
#                 if(existing_user.is_active == False):
#                     existing_user.delete()
#             except:
#                 pass


from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from users.forms import CustomAuthenticationForm,CustomerPictureForm
from .models import Customer,Seller,CustomerAdditional
# class Login(LoginView):

#     authentication_form = CustomAuthenticationForm

#     form_class = CustomAuthenticationForm

#     template_name = 'login.html'

#     def form_valid(self, form):

#         remember_me = form.cleaned_data['remember_me']

#         login(self.request, form.get_user())

#         if remember_me:

#             self.request.session.set_expiry(1209600)

#         return super(LoginView, self).form_valid(form)
def CustomerRegistrationView(request):
    form = RegistrationFormCustomer(request.POST,None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful." )
        return redirect("customer_profile")
    
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=RegistrationFormCustomer()
    return render (request, template_name="registercustomer.html", context={"form":form})

# def SellerRegistrationView(request):
#     form = RegistrationFormSeller(request.POST)
#     if form.is_valid():
#         user = form.save()
#         login(request, user)
#         messages.success(request, "Registration successful." )
#         return redirect("seller_profile")
    
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     else:
#         form=RegistrationFormSeller()
#     return render (request, template_name="registerseller.html", context={"form":form})
    

def Login(request):
    # if request.user.is_authenticated and  request.user.is_customer is True:
    #     messages.info(request, message='you are already logged in')
    #     return redirect('customer_profile')
    # else:
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            print(user.type)
            if user.Types.CUSTOMER:
                if user is not None: 
                    request.session['customer'] = user.id
                    if user.is_customer is True:
                        login(request, user)
                    
                        if remember_me:
                            request.session.set_expiry(1209600)
                        messages.info(request, f"You are now logged in as {username}")
                        return redirect('customer_profile')
                    else:
                            messages.error(request, "Invalid username or password.")
                else:
                    messages.error(request, "Invalid username or password.")
            # elif  user.Types.SELLER:
            #     if user is not None:
            #         print(user.name) 
            #         login(request, user)
            #         if remember_me:
            #             request.session.set_expiry(1209600)
            #         messages.info(request, f"You are now logged in as {username}")
            #         return redirect('seller_profile')
            #     else:
            #         messages.error(request, "Invalid username or password.")
            # else:
            #     messages.warning(request, message='you are not validate user')
        else:
            messages.error(request, "Invalid username or password.")
    form = CustomAuthenticationForm()
    
    return render(request, template_name='login.html' ,context={'form':form})



@login_required
def ProfilePictureUpdate(request):
    if request.method == "POST":
        # u_form=CustomerUpdateForm(request.POST,instance=request.user)
        p_form=CustomerPictureForm(request.POST,request.FILES,instance=request.user)
        
        if  p_form.is_valid():
            p_form.save()
            messages.success(request,'your profile picture have been updated')
            return redirect('customer_profile')
    else:
        # u_form=CustomerUpdateForm(instance=request.user)
        p_form=CustomerPictureForm(instance=request.user)
        
    return render(request,template_name='profile_picture_update.html',context = {'p_form':p_form})


@login_required(redirect_field_name='login')
def CustomerProfileView(request):
    if request.method == "POST":
        # u_form=CustomerUpdateForm(request.POST,instance=request.user)
        p_form=CustomerPictureForm(request.POST,request.FILES,instance=request.user)
        
        if  p_form.is_valid():
            p_form.save()
            messages.success(request,'your profile picture have been updated')
            return redirect('customerr_profile')
    else:
        # u_form=CustomerUpdateForm(instance=request.user)
        p_form=CustomerPictureForm(instance=request.user)
        
    return render(request,template_name='customer_profile.html',context = {'p_form':p_form}) 
 
@login_required
def updateprofile(request):
    if request.method == "POST":
        u_form=CustomerUpdateForm(request.POST,instance=request.user)
        p_form=CustomerPictureForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request,'you have been updated')
            return redirect('customer_profile')
    else:
        u_form=CustomerUpdateForm(instance=request.user)
        # p_form=CustomerPictureForm(instance=request.user)
        
    return render(request,template_name='update_profile.html',context = {'u_form':u_form})   



class sellerProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'suplier_profile.html')

@login_required
def logout_request(request):
   
    logout(request)
    messages.info(request, "You have been successfully logged out ") 
    return redirect("login")
    
# def SellerRegistrationView(request):
#     form=RegistrationFormSeller(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#         messages.success(request,message='registrations successfully done')
#     else:
#         form=RegistrationFormSeller()
#         messages.warning(request,message="something wrong")
    
    
#     return render(request, template_name='registerbasicuser.html' ,context={'form':form})

    # def post(self, request, *args, **kwargs):
    #     #form = RegistrationForm(request.POST)
    #     user_email = request.POST.get('email')
    #     try:
    #         existing_user = CustomUser.objects.get(email = user_email)
    #         if(existing_user.is_active == False):
    #             existing_user.delete()
    #     except:
    #         pass
    #     response = super().post(request, *args, **kwargs)
    #     if response.status_code == 302:
    #         user = CustomUser.objects.get(email = user_email)
    #         user.is_active = False
    #         user.save()
    #         current_site = get_current_site(request)     #www.wondershop.in:8000  127.0.0.1:8000 
    #         mail_subject = 'Activate your account.'
    #         message = render_to_string('firstapp/registration/acc_active_email.html', {
    #             'user': user,
    #             'domain': current_site.domain,
    #             'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    #             'token':account_activation_token.make_token(user),
    #         })
    #         #print(message)
    #         to_email = user_email   
    #         #form = RegistrationForm(request.POST)   # here we are again calling all its validations
    #         form = self.get_form()
    #         try:
    #             send_mail(
    #                 subject=mail_subject,
    #                 message=message,
    #                 from_email=settings.EMAIL_HOST_USER,
    #                 recipient_list= [to_email],
    #                 fail_silently=False,    # if it fails due to some error or email id then it get silenced without affecting others
    #             )
    #             messages.success(request, "link has been sent to your email id. please check your inbox and if its not there check your spam as well.")
    #             return self.render_to_response({'form':form})
    #         except:
    #             form.add_error('', 'Error Occured In Sending Mail, Try Again')
    #             messages.error(request, "Error Occured In Sending Mail, Try Again")
    #             return self.render_to_response({'form':form})
    #     else:
    #         return response



# class LoginViewUser(LoginView):
#     template_name = "firstapp/login.html"
    #success_url = reverse_lazy('index')





# class RegisterViewSeller(LoginRequiredMixin, CreateView):
#     template_name = 'firstapp/registerseller.html'
#     form_class = RegistrationFormSeller2
#     success_url = reverse_lazy('index')

#     def form_valid(self, form):
#         user = self.request.user
#         user.type.append(user.Types.SELLER)
#         user.save()
#         form.instance.user = self.request.user
#         return super().form_valid(form)
        

# class LogoutViewUser(LogoutView):
#     success_url = reverse_lazy('index')
