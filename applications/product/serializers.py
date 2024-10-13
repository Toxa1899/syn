from rest_framework import serializers

from applications.product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SalesmanAdditionallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
