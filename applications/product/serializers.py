from rest_framework import serializers

from applications.product.models import (
    Category,
    Product,
    SalesmanAdditionally,
    Salesman,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_data = CategorySerializer(read_only=True, source="category")

    class Meta:
        model = Product
        fields = "__all__"


class SalesmanSerializer(serializers.ModelSerializer):
    products_data = ProductSerializer(
        many=True, read_only=True, source="products"
    )

    class Meta:
        model = Salesman
        fields = "__all__"


class SalesmanAdditionallySerializer(serializers.ModelSerializer):
    salesman_data = SalesmanSerializer(read_only=True, source="salesman")

    class Meta:
        model = SalesmanAdditionally
        fields = "__all__"

    def validate_salesman(self, salesman):
        if SalesmanAdditionally.objects.filter(salesman=salesman).exists():
            raise serializers.ValidationError(
                "Описание к данному пользователю уже существует"
            )
        return salesman
