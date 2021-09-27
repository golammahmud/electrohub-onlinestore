from django.contrib import admin
from shop.models import Orders,Subcategory,Product,MyShop,Banar,ProductFeatures,Banar_carnival,Newsletter,ProductFacility


from .models import ProductImage


class ProductFacilityAdmin(admin.StackedInline):
    model=ProductFacility

class ProductFeatureAdmin(admin.StackedInline):
    model=ProductFeatures
    
class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines=[ProductImageAdmin,ProductFeatureAdmin,ProductFacilityAdmin]
    
    
    list_display=('post_images','name','price','is_approved','stock','category','is_featured','suplier','date_created')
    list_filter=('name','price','category','is_approved','is_featured','suplier' )
    list_editable=('stock','is_approved','is_featured' ,)
    list_display_links=('post_images','name','price','category','suplier' )
#      list_display_links=('post_images','user',)
    search_fields=('name','is_approved','price','category','suplier' )
    read_only_fields=('post_images' )
    # fieldsets=((None,{
    #       'fields':(
    #            'name', 
    #            'slug',
    #            'price',
    #            ' del_price'
    #            'product_type',
    #            'stock',
    #            'category',
    #            'description',
    #            'image',
    #            'suplier',
    #            'date_created'
    #       )
    #  }),
    #             )
    
    class Meta:
        model=Product

@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    pass    
@admin.register(Banar)
class ProductBanar(admin.ModelAdmin):
    pass    


@admin.register(Banar_carnival)
class Banar_carnival(admin.ModelAdmin):
    pass

@admin.register(Newsletter)
class NewsLetter(admin.ModelAdmin):
    list_display=('email','date_added',)
@admin.register(Subcategory)
class Category(admin.ModelAdmin):
    list_display=('post_images','name','parent','is_featured',)
    list_filter=('name','parent','is_featured' )
    list_editable=('is_featured',)
    list_display_links=('post_images','name', )
#      list_display_links=('post_images','user',)
    search_fields=('name', 'parent')
    read_only_fields=('post_images' )
    fieldsets=((None,{
          'fields':(
               'parent',
               'name', 
               'slug',
               'image',
               'is_featured',
          )
     }),
                )
    
@admin.register(Orders)
class Orders(admin.ModelAdmin):
    pass
@admin.register(MyShop)
class OnlineShop(admin.ModelAdmin):
    list_display=('name','email','phone','address',)
    
