from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError
from django.core import validators
# from user.models import Customer,Suplier

from io import BytesIO
from django.core.files import File
from PIL import Image
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from users.models import CustomUser,Seller

from django.urls import reverse


def validations_email(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError('email is not valid')
def validate(self):
    name=self.name
    address=self.address
    if name=='parvez' and address!='pabna':
        raise ValidationError('adress must be pabna')
    

class MyShop(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validators.EmailValidator])
    phone = PhoneNumberField(default='+880-')
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100,default='Bangladesh')

    def __str__(self):
        return self.name
class Banar_carnival(models.Model):
    carnival_title=models.CharField(max_length=100)
    carnival_offer_title=models.CharField(max_length=100)
    banar_height=models.FloatField(blank=True,null=True)
    banar_width=models.FloatField(blank=True,null=True)
    image=models.ImageField(blank=True,upload_to='shop/product/banar',height_field='banar_height',width_field='banar_width')

    def __str__(self):
        return self.carnival_title
    
class Banar(models.Model):
    product_title=models.CharField(max_length=100)
    offer_title=models.CharField(max_length=100)
    banar_height=models.FloatField(blank=True,null=True)
    banar_width=models.FloatField(blank=True,null=True)
    image=models.ImageField(blank=True,upload_to='shop/product/banar',height_field='banar_height',width_field='banar_width')
    offer_spain=models.CharField(blank=True,null=True,max_length=100)
    btn_title=models.CharField(max_length=50,blank=True,null=True,default='Shop Now')
    def __str__(self):
        return self.product_title
    


class Subcategory(models.Model):
    parent=models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',blank=True,null=True)
    name=models.CharField(max_length=150,unique=True,default=None,null=False)
    slug=models.SlugField(max_length=150,unique=True)
    image=models.ImageField(blank=True,upload_to='shop/product/category/images')
    is_featured=models.BooleanField(default=False)
    
  
    class Meta:
        verbose_name_plural = 'Subcategories'
        ordering = ('-id',)
    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def post_images(self):
        return mark_safe('<img src="{}" width="100" hieght="100" />' .format(self.image.url))
    post_images.short_description='Profile picture'
    post_images.alow_tags=True
    
    
    @staticmethod
    def get_all_subcategories():
        return Subcategory.objects.all()
    
    def __str__(self):
        return self.name
    
    # def save(self,*args,**kwargs):
    #     self.image=self.make_thumbnail(self.image)
    
    #     super().save(*args, **kwargs)
        
    
    # def make_thumbnail(self, image, size=(160, 160)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)
    
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=95)
    
    #     thumbnail = File(thumb_io, name=image.name)
    
    #     return thumbnail



class Product(models.Model):
    # stock_choices = [
    #     ('AV', 'Avaible'),
    #     ('NAV', 'Not avaible'),
    #     ('LTD', 'Limited'),
    # ]
    product_type=[
        ('New','New'),
        ('Latest','Latest')
    ]
    width=200
    height=200
   
   
    category = models.ForeignKey(Subcategory,related_name="products" ,on_delete=models.CASCADE) 
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True) 
    # variasions=models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',blank=True,null=True)
    name = models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,unique=True)
    price = models.IntegerField(default=0)
    currency=models.CharField(max_length=50,default='', null=True ,blank=True)
    del_price=models.CharField(max_length=50,null=True,blank=True)
    offers_price=models.CharField(max_length=60,null=True,blank=True)
    product_type=models.CharField(max_length=70,null=True,blank=True,choices=product_type)
    stock = models.IntegerField(default=1,null=True,blank=True)
    description = models.TextField(verbose_name='description')
    image=models.ImageField(blank=True,upload_to='shop/product/images',width_field='width',height_field='height')
    # image=models.FileField(blank=True,upload_to='shop/product/images,')
    # image = models.ImageField(blank=True, verbose_name='images', max_length=200, upload_to='shop/images', null=True)
    # suplier = models.ManyToManyField(Seller, related_name='suplier' ,default='Admin')
    suplier = models.ForeignKey(Seller, related_name='products',default='admin@gmail.com' ,on_delete=models.CASCADE)
    num_visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    
    is_featured=models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('update_product',kwargs={'slug':self.slug})
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    
    @staticmethod
    def get_all_product():
        return Product.objects.all().order_by('product')
    
    @staticmethod 
    def get_all_product_by_category(category_slug):
        if category_slug:
            return Product.objects.filter(category=category_slug)
        else:
            return Product.objects.all().order_by('product')
        
    def __str__(self):
        return self.name
    
    # def save(self,*args,**kwargs):
    #     self.image=self.make_thumbnail(self.image)
    
    #     super().save(*args, **kwargs)
        
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
    
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)
    
        thumbnail = File(thumb_io, name=image.name)
    
        return thumbnail
    
    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def post_images(self):
        return mark_safe('<img src="{}" width="100" hieght="100" />' .format(self.image.url))
    post_images.short_description='Profile picture'
    post_images.alow_tags=True


class ProductFacility(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None ,related_name='product_facility')
    facility=models.TextField(verbose_name='facility',blank=True,null=True)
    def __str__(self):
        return self.product.name
    
class ProductFeatures(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None,related_name='product_feature')
    feature=models.TextField(verbose_name='feature',blank=True,null=True)
    def __str__(self):
        return self.product.name
    
class ProductImage(models.Model):
    width=350
    height=400
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None,related_name='product_images')
    images=models.ImageField(upload_to='shop/product/images',height_field='height',width_field='width')
    def __str__(self):
        return self.product.name

class Orders(models.Model):
    product_id = models.ManyToManyField(Product, related_name='product')
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    deliverystatus = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    orderdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id



 
    
    # def __str__(self):
    #     return f'{self.user.username} profile'
    
   
    
    # def save(self):
    #     super().save()
        
    #     img=Image.open(self.images.path)
    #     if img.height>400 or img.width>400:
    #         output_size=(400,400)
    #         img.thumbnail(output_size)
    #         img.save(self.images.path)
    
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    
class Newsletter(models.Model):
    email = models.EmailField(blank=True,validators=[validators.EmailValidator])
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email