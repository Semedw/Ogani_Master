from core.models import *
from rest_framework import serializers


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'weight', 'color', 'size', 'heart', 'retweet', 'category')



class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'image', 'shipping_time', 'weight', 'color', 'size', 'free_pickup')


