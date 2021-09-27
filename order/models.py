# from django.db import models
# from users.models import Customer
# from shop.models import Product

# class Order(models.Model):
#     ORDERED = 'ordered'
#     SHIPPED = 'shipped'
#     ARRIVED = 'arrived'

#     STATUS_CHOICES = (
#         (ORDERED, 'Ordered'),
#         (SHIPPED, 'Shipped'),
#         (ARRIVED, 'Arrived')
#     )

#     user = models.ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     place = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)

#     created_at = models.DateTimeField(auto_now_add=True)

#     paid = models.BooleanField(default=False)
#     paid_amount = models.FloatField(blank=True, null=True)
#     used_coupon = models.CharField(max_length=50, blank=True, null=True)

#     payment_intent = models.CharField(max_length=255)

#     shipped_date = models.DateTimeField(blank=True, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

#     def __str__(self):
#         return '%s' % self.first_name
    
#     def get_total_quantity(self):
#         return sum(int(item.quantity) for item in self.items.all())
    
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
#     price = models.FloatField()
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return '%s' % self.id



from django.db import models
from shop.models import Product
from users.models import Customer,Seller

import datetime
from django.utils import timezone
from django.urls import reverse


class Order(models.Model):
    CANCEL = 'cancel'
    PENDING = 'pending'
    RECIVED = 'recived'
    STATUS_CHOICES = (
        (CANCEL, 'cancel'),
        (PENDING,  'pending'),
        (RECIVED, 'recived')
    )
    
 
    product = models.ForeignKey(Product, related_name='orders',
                                on_delete=models.CASCADE )
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20,decimal_places=15)
    address = models.CharField(max_length=250, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    order_area=models.CharField(max_length=250, default='', blank=True)
    # date = models.DateField(default=datetime.datetime.today)
    order_status=models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    status = models.BooleanField(default=False,null=True,blank=True)
    vendor= models.ManyToManyField(Seller, related_name='orders')
    CASH_ON_DELIVERY = 'cash_on_delivery'
    CARD = 'card'
    
    PAYMENT_STATUS_CHOICES = (
      (CASH_ON_DELIVERY ,'cash_on_delivery'),
   ( CARD ,'card'),
    )
    
    payment_status=models.CharField(null=True,blank=True,max_length=20, choices=PAYMENT_STATUS_CHOICES, default=CASH_ON_DELIVERY)
    date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('product_order_update',kwargs={'pk':self.pk})
    
    def placeOrder(self):
        self.save()
        
        

    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
    @staticmethod
    def get_orders_by_seller(seller_id):
        return Order.objects.filter(vendor=seller_id).order_by('-id')
    
    
    def __str__(self):
        return self.product.name
    
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Seller, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s' % self.id
    
    @staticmethod
    def get_orderitem_by_seller(order_id):
        return OrderItem.objects.filter(order__in=order_id ).order_by('-product')
       
    
    
    def get_total_price(self):
        return self.price * self.quantity