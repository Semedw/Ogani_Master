from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
)


from core.api.serializers import GetProductSerializer, CreateProductSerializer
from core.models import (
    Product,
)


class GetProductAPIView(ListAPIView):
    serializer_class = GetProductSerializer
    queryset = Product.objects.all()


class CreateProductAPIView(CreateAPIView):
    serializer_class = CreateAPIView
    queryset = Product.objects.all()