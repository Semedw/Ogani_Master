from django.urls import path

from core.views import (index, shop, blog, contact, shop_details, 
                        blog_details, checkout, shopping_cart,
                        discount_details, departments,
)

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('shop-details/<slug:slug>/', shop_details, name='shop_details' ),
    path('blog-details/<slug:slug>/', blog_details, name='blog_details'),
    path('checkout/', checkout, name='checkout'),
    path('shopping-cart/', shopping_cart, name='shopping_cart'),
    path('discount-details/<slug:slug>/', discount_details, name='discount_details'),
    path('departments/<slug:slug>', departments, name='departments')
    
]
