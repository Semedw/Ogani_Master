from django.urls import path

from core.api.views import (
    GetProductAPIView, CreateProductAPIView
)

urlpatterns = [
    path('news/', GetProductAPIView.as_view(), name='get_view'),

]