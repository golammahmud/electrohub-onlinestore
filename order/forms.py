from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget

from order.models import Order

from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class OrderForm(forms.ModelForm):
    # image=MultiMediaField(min_num=1,max_num=3,max_file_size=1024*1024*5,media_type='image' or'video' or 'audio')
    class Meta:
        model = Order
        fields=['address','phone','order_area','order_status','payment_status']
        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})
                   }
    
class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='__all__'
        
