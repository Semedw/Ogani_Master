from core.models import *
from rest_framework import routers, serializers



# Product Serializers


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'weight', 'color', 'size', 'heart', 'retweet', 'category')



class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'image', 'shipping_time', 'weight', 'color', 'size', 'free_pickup')


class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'image', 'shipping_time', 'weight', 'color', 'size', 'free_pickup')


# Blog Serializers


class GetBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'comment', 'category')


class CreateBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', )


class UpdateBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', )


# Product Category Serializers


class GetProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('title', 'image', )


# Blog Category Serializers


class GetBlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogCategory
        fields = ('title', )


# Banner Serializer


class GetBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ('title', 'description', 'category', 'img')


class CreateBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ('title', 'description', 'category', 'img')


class UpdateBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ('title', 'description', 'category', 'img')


# Settings Serializer


class GetSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ('address', 'phone', 'e_mail')


# Contact Serializer 


class GetContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


# Color Serializer

class GetColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        fields = ('title', )


# Size Serializer


class GetSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('title', )

class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Subscriber
        fields = ['email',]