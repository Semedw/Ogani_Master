from django.urls import path

from core.api.views import *


urlpatterns = [
    path('get-product/', GetProductAPIView.as_view(), name='get_product'),
    path('create-product/', CreateProductAPIView.as_view(), name='create_product'),
    path('update-product/', UpdateProductAPIView.as_view(), name='update_product'),
    path('get-blog/', GetBlogAPIView.as_view(), name='get_blog'),
    path('create-blog/', CreateBlogAPIView.as_view(), name='create_blog'),
    path('update-blog/', UpdateBlogAPIView.as_view(), name='update_blog'),
    path('get-product-category/', GetProductCategoryAPIView.as_view(), name='get_product_category'),
    path('get-blog-category/', GetBlogCategoryAPIView.as_view(), name='get_blog_category'),
    path('get-banner/', GetBannerAPIView.as_view(), name='get_product'),
    path('create-banner/', CreateBannerAPIView.as_view(), name='get_product'),
    path('update-banner/', UpdateBannerAPIView.as_view(), name='get_product'),
    path('get-settings/', GetSettingsAPIView.as_view(), name='get_product'),
    path('get-contact/', GetContactAPIView.as_view(), name='get_product'),
    path('get-color/', GetColorAPIView.as_view(), name='get_product'),
    path('get-size/', GetSizeAPIViews.as_view(), name='get_product'),
    # path('get-subscriber/', GetSubscriberAPIViews.as_view(), name='get_subscriber'),
    # path('create-subscriber/', CreateSubscriberAPIViews.as_view(), name='create_subscriber'),
    # path('update-subscriber/', UpdateSubscriberAPIViews.as_view(), name='update_subscriber'),
    path('subscriber/', SubsciberApiView.as_view(), name='subscriber'),
]
