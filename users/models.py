from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.core import validators
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.
from multiselectfield import MultiSelectField


from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

from django.contrib.auth.models import PermissionsMixin

from django.db.models import Q
from datetime import timedelta
from django.utils import timezone

def validations_email(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError('email is not valid')
    
class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = None
    email = LowercaseEmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    is_seller= models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # if you require phone number field in your project
    # phone_regex = RegexValidator( regex = r'^\d{11}$',message = "phone number should exactly be in 10 digits")
    # phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True
    phone=PhoneNumberField(default='+880')
    profession=models.CharField(max_length=500,default='')
    address = models.CharField(max_length=1000,default='')
    Company_name = models.CharField(max_length=250 ,default='')
    warehouse_location = models.CharField(max_length=1000 ,default='')
    goodstype=models.CharField(max_length=250 ,default='')
    images=models.ImageField(upload_to='profile/images' ,verbose_name='profile_pic',max_length=200,default='profile.jpg',blank=True)
    email_confirmed = models.BooleanField(default=False)
    class Meta:
        ordering=('-pk',)
        
        
    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def post_images(self):
        return mark_safe('<img src="{}" width="100" hieght="100" />' .format(self.images.url))
    post_images.short_description='Profile picture'
    post_images.alow_tags=True
    # def save(self):
    #     super().save()
    
    #     img=Image.open(self.images.path)
    #     if img.height>400 or img.width>400:
    #         output_size=(400,400)
    #         img.thumbnail(output_size)
    #         img.save(self.images.path)
    
    
    
    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default = False)

    # type = (
    #     (1, 'Seller'),
    #     (2, 'Customer')
    # )
    # user_type = models.IntegerField(choices = type, default=1)

    #usertype = models.ManyToManyField(UserType)

    class Types(models.TextChoices):
       
        CUSTOMER = "Customer", "CUSTOMER"
        SELLER = "Seller", "SELLER"
    
    # Types = (
    #     (1, 'SELLER'),
    #     (2, 'CUSTOMER')
    # )
    # type = models.IntegerField(choices=Types, default=2)
    types=list[Types.CUSTOMER]
    default_type = types
    

    #type = models.CharField(_('Type'), max_length=255, choices=Types.choices, default=default_type)
    type = MultiSelectField(choices=Types.choices, default=[], null=True, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    #place here
        # if not the code below then taking default value in User model not in proxy models
    def save(self, *args, **kwargs):
        if not self.id:
            #self.type = self.default_type
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)
    
class CustomerAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    phone=PhoneNumberField(default='+880')
    address = models.CharField(max_length=1000)
    images=models.ImageField(upload_to='customer_profile/images' ,verbose_name='profile_pic',max_length=200,default='profile.jpg',blank=True)

    
    
class SellerAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    phone=PhoneNumberField(default='+880')
    gst = models.CharField(max_length=10)
    warehouse_location = models.CharField(max_length=1000)
    

# Model Managers for proxy models
class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.SELLER))

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.CUSTOMER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.CUSTOMER))
# Proxy Models. They do not create a seperate table
class Seller(CustomUser):
    default_type = CustomUser.Types.SELLER
    objects = SellerManager()
    class Meta:
        proxy = True
    
    def sell(self):
        print("I can sell")

    @property
    def showAdditional(self):
        return self.selleradditional

class Customer(CustomUser):
    default_type = CustomUser.Types.CUSTOMER
    objects = CustomerManager()
    class Meta:
        proxy = True 

    def buy(self):
        print("I can buy")

    @property
    def showAdditional(self):
        return self.customeradditional
    
    


class Profile(models.Model):
    user=models.OneToOneField(CustomUser,related_name='profile',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='profile/images' ,verbose_name='profile_pic',max_length=200,default='profile.jpg',blank=True)
    email_confirmed = models.BooleanField(default=False)
    class Meta:
        ordering=('-pk',)
        
        
    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def post_images(self):
        return mark_safe('<img src="{}" width="100" hieght="100" />' .format(self.images.url))
    post_images.short_description='Profile picture'
    post_images.alow_tags=True
    
    
    
    def __str__(self):
        return f'{self.user.name} profile'
    
    
    
class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    msg=models.TextField(verbose_name='message')
    date_added=models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return  self.firstname + self.lastname
    









