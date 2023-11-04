from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.api.serializers import *
from core.models import *


# Product Views
class GetProductAPIView(ListAPIView):
    serializer_class = GetProductSerializer
    queryset = Product.objects.all()


class CreateProductAPIView(CreateAPIView):
    serializer_class = CreateAPIView
    queryset = Product.objects.all()


class UpdateProductAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateProductSerializer
    queryset = Product.objects.all()


# Blog Views
class GetBlogAPIView(ListAPIView):
    serializer_class = GetBlogSerializer
    queryset = Blog.objects.all()


class CreateBlogAPIView(CreateAPIView):
    serializer_class = CreateBlogSerializer
    queryset = Blog.objects.all()


class UpdateBlogAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateBlogSerializer
    queryset = Blog.objects.all()


# Product Category Views
class GetProductCategoryAPIView(ListAPIView):
    serializer_class = GetProductCategorySerializer
    queryset = ProductCategory.objects.all()


# Blog Category Views
class GetBlogCategoryAPIView(ListAPIView):
    serializer_class = GetBlogCategorySerializer
    queryset = BlogCategory.objects.all()


# Banner Views
class GetBannerAPIView(ListAPIView):
    serializer_class = GetBannerSerializer
    queryset = Banner.objects.all()


class CreateBannerAPIView(CreateAPIView):
    serializer_class = CreateBannerSerializer
    queryset = Banner.objects.all()


class UpdateBannerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateBannerSerializer
    queryset = Banner.objects.all()


# Settings Views
class GetSettingsAPIView(ListAPIView):
    serializer_class = GetSettingsSerializer
    queryset = Settings.objects.all()


# Contact Views
class GetContactAPIView(ListAPIView):
    serializer_class = GetContactSerializer
    queryset = Contact.objects.all()


# Color Views
class GetColorAPIView(ListAPIView):
    serializer_class = GetColorSerializer
    queryset = Colors.objects.all()


# Size Views
class GetSizeAPIViews(ListAPIView):
    serializer_class = GetSizeSerializer
    queryset = Size.objects.all()


# class GetSubscriberAPIViews(ListAPIView):
#     serializer_class = GetSubscriberSerializer
#     queryset = Subscriber.objects.all()


# class CreateSubscriberAPIViews(CreateAPIView):
#     serializer_class = CreateSubscriberSerializer
#     queryset = Subscriber.objects.all()


# class UpdateSubscriberAPIViews(RetrieveUpdateDestroyAPIView):
#     serializer_class = UpdateSubscriberSerializer
#     queryset = Subscriber.objects.all()


class SubsciberApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)