from django.urls import include, path

# from users.views import classroom, students, teachers
from users.views import CustomerProfileView,sellerProfileView,CustomerRegistrationView,updateprofile,ProfilePictureUpdate,contact
urlpatterns = [
    # path('seller/registration/',SellerRegistrationView, name='seller_registrations'),
        
    
    path('customer/registration/',CustomerRegistrationView, name='customer_registrations'),
    path('customer/profile/', CustomerProfileView, name='customer_profile'),
    # path('seller/profile/', sellerProfileView.as_view(), name='seller_profile'),
    path('update/customer-profile',updateprofile ,name='update_customer_profile'),
    path('user/update-photo',ProfilePictureUpdate,name='update_picture'),
  
  
]