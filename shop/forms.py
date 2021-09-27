from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget

from shop.models import OnlineShop,Product
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


# If you need to upload media files, you can use this:
    # image= MultiMediaField(
    #     min_num=1,
    #     max_num=3,
    #     max_file_size=1024*1024*5,
    #     media_type='video'  # 'audio', 'video' or 'image'
    # )

class ProductForm(forms.ModelForm):
    image=MultiMediaField(min_num=1,max_num=3,max_file_size=1024*1024*5,media_type='image' or'video' or 'audio')
    class Meta:
        model = Product
        fields='__all__'
    
    


class OnlineShopForm(forms.ModelForm):

    class Meta:
        model = OnlineShop
        fields = '__all__'

        widgets = {'phone': PhoneNumberPrefixWidget(initial='BD',
            attrs={'placeholder': (u'Enter Your phone Number'), 'class': "form-control", 'style': 'display:grid'})

                   }


