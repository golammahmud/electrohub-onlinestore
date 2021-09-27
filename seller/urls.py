
from django.contrib import admin
from django.urls import path, include
from .views import (SellerView,SellerRegistrationView,SellerLogin,sellerProfileView,logout_request,
                    ProfilePictureUpdate,UpdateSellerProfile,CreateProduct,CreateSellerProduct,
                    CreateSellerProductView,Add_image_feature_Product,Seller_Product
                    ,Edit_Product,ProductUpdate,DeleteProduct,OrderView,prodect_details,
                    OrderStatusUpdateView,AllOrder)
urlpatterns = [
    
    
    path('', SellerView ,name='seller'),
    
    # path('<int:pk>/order/update', OrderStatusUpdateView.as_view(), name='product_order_update'),
    
    
    path('signup/', SellerRegistrationView ,name='signup'),
    path('signin/', SellerLogin ,name='signin'),
    path('profile/', sellerProfileView.as_view() ,name='seller_profile'),
    path('logout/', logout_request ,name='logout'),
    path('Update-profile-picture/', ProfilePictureUpdate ,name='picture_update'),
    path('Update-profile/', UpdateSellerProfile ,name='seller_profile_update'),
   # path('upload_product/', CreateProduct.as_view() ,name='create_product'),
    path('upload_product/', CreateSellerProduct ,name='create_product'),
    #path('upload_product/', CreateSellerProductView.as_view() ,name='create_product'),
    path('product/order/', OrderView, name='product_order'),
    
    path('all/orders', AllOrder, name='all_orders'),
    
    
    path('<int:id>/order/update', OrderStatusUpdateView, name='product_order_update'),
    
    
    path('products/', Seller_Product, name='seller_Product'),
    path('<slug:slug>/update', Add_image_feature_Product, name='update_product'),
     path('<slug:slug>/edit', Edit_Product, name='edit_product'),
    # path('<slug:slug>/edit', ProductUpdate.as_view(), name='edit_product'),
    path('<slug:slug>/delete', DeleteProduct.as_view(), name='delete_product'),
    path('<slug:category_slug>/<slug:slug>/',prodect_details,name='product_detail'),
    
    
  
    

 
] 