# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction

# from .models import Seller, Customer, CustomUser

# class CustomerSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=Customer.objects.all(),
#         # widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         user.save()
#         customer= Customer.objects.create(user=user)
#         customer.interests.add(*self.cleaned_data.get('interests'))
#         return user
# class SellerSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_seller = True
#         if commit:
#             user.save()
#         return user


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer, Seller, SellerAdditional,Contact
from django import forms
from django.core.validators import RegexValidator
from django.db import transaction

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
        ]

class RegistrationFormSeller(UserCreationForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'phone',
            'address',
            'Company_name',
            'warehouse_location',
            'goodstype',
            'password1',
            'password2',
        ]
        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})
                   }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        return user
    
    
class SellerProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'phone',
            'address',
            'Company_name',
            'warehouse_location',
            'goodstype',
            'images',
           
        ]
        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})
                   }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        return user
class RegistrationFormSeller2(forms.ModelForm):
    class Meta:
        model = SellerAdditional
        fields = [
            'gst',
            'warehouse_location'
        ]


class SendOtpBasicForm(forms.Form):
    phone_regex = RegexValidator( regex = r'^\d{11}$',message = "phone number should exactly be in 11 digits")
    phone = forms.CharField(max_length=255, validators=[phone_regex])

    class Meta:
        fields = [
            'phone',
        ]

class VerifyOtpBasicForm(forms.Form):
    otp_regex = RegexValidator( regex = r'^\d{4}$',message = "otp should be in six digits")
    otp = forms.CharField(max_length=6, validators=[otp_regex])

    # class Meta:
    #     field





class RegistrationFormCustomer(UserCreationForm):
    class Meta:
        model = Customer
        fields = [
            'email',
            'name',
            'phone',
            'address',
            'profession',
            'password1',
            'password2',
        ]
        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})
                   }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer= True
        user.save()
        return user
    

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'email',
            'name',
            'phone',
            'address',
            'profession',
            'images'
        ]
        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})
                   }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer= True
        user.save()
        return 



class CustomerPictureForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'images'
        ]
class sellerPictureForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'images'
        ]
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class': 'checkbox ' ,'style':'margin-left:120px;'}))
    
    
class CustomerAuthenticationForm(RegistrationFormCustomer):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True,'style':'margin-bottom:50px; '}))
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class': 'checkbox ' ,'style':'margin-left:120px; '}))
class SellerAuthenticationForm(RegistrationFormSeller):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True ,'style':'margin-bottom:50px; '}))
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class': 'checkbox ' ,'style':'margin-left:120px; '}))



class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'