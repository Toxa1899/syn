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

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def notify_users(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications", {"type": "send_notification", "message": message}
    )


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        notify_users({"text": f"создана новая категория: --> {instance.name}"})


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        notify_users({"text": f"создан новый продукт: -->  {instance.name}"})


class SalesmanModelViewSet(ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class SalesmanAdditionallyModelViewSet(ModelViewSet):
    queryset = SalesmanAdditionally.objects.all()
    serializer_class = SalesmanAdditionallySerializer


def index(request):
    return render(request, "index.html")
