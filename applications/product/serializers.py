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
    class Meta:
        model = Product
        fields = "__all__"


class SalesmanSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    products_w = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Salesman
        fields = ["id", "name", "products", "products_w"]

    def create(self, validated_data):
        products = validated_data.pop("products_w")
        salesman = Salesman.objects.create(**validated_data)
        salesman.products.set(products)
        return salesman

    def update(self, instance, validated_data):
        products = validated_data.pop("products_w", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if products:
            instance.products.set(products)
        instance.save()
        return instance


class SalesmanAdditionallySerializer(serializers.ModelSerializer):
    salesman = SalesmanSerializer(read_only=True)
    salesman_w = serializers.PrimaryKeyRelatedField(
        queryset=Salesman.objects.all(), write_only=True
    )

    class Meta:
        model = SalesmanAdditionally
        fields = "__all__"

    def create(self, validated_data):

        salesman_instance = validated_data.pop("salesman_w")

        validated_data["salesman"] = salesman_instance
        return SalesmanAdditionally.objects.create(**validated_data)

    def update(self, instance, validated_data):

        salesman_instance = validated_data.pop("salesman_w", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if salesman_instance:
            instance.salesman = salesman_instance

        instance.save()
        return instance
