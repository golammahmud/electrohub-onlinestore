from django.contrib import admin
from order.models import Order,OrderItem
# Register your models here.
@admin.register(Order)
class Banar_carnival(admin.ModelAdmin):
    list_display=('customer','quantity','price','phone','order_area','status')
    list_filter=('customer','price','status' )
    list_editable=('status',)
    list_display_links=('customer','price', )
#      list_display_links=('post_images','user',)
    # search_fields=('product',)
    # read_only_fields=('product' )
    # fieldsets=((None,{
    #       'fields':(
    #            'parent',
    #            'name', 
    #            'slug',
    #            'image',
    #            'is_featured',
    #       )
    #  }),
    #             )
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','product','vendor','vendor_paid','price','quantity')
    