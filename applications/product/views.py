from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.product.models import (
    Category,
    Product,
    Salesman,
    SalesmanAdditionally,
)
from applications.product.serializers import (
    CategorySerializer,
    ProductSerializer,
    SalesmanAdditionallySerializer,
    SalesmanSerializer,
)


# Create your views here.


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SalesmanModelViewSet(ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class SalesmanAdditionallyModelViewSet(ModelViewSet):
    queryset = SalesmanAdditionally.objects.all()
    serializer_class = SalesmanAdditionallySerializer
