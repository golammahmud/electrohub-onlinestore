from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget

from shop.models import Product,ProductFacility,ProductFeatures,ProductImage

from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

# from betterforms.multiform import MultiModelForm

class SellerProduct(forms.ModelForm):
    class Meta:
        model=Product
        fields=['category','parent','name','slug','price','currency','del_price','offers_price','product_type','stock','description','image','is_featured']
        
        

class ProductFacilityForm(forms.ModelForm):
    class Meta:
        model=ProductFacility
        fields=['facility']
        
class ProductFeaturesForm(forms.ModelForm):
    class Meta:
        model=ProductFeatures
        fields=['feature']
        
        
class ProductImageForm(forms.ModelForm):
    images= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=ProductImage
        fields=['images']
        
        # widgets = {'images': forms.ImageField(attrs={'multiple': True})}
        
        
        
# class SellerMultiForm(MultiModelForm):
#     form_classes = {
#         'product': SellerProduct,
#         'facility': ProductFacility,
#         'feature':ProductFeatures,
#         'images':ProductImage
#     }