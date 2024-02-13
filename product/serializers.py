from rest_framework import serializers
from product.models import ShoppingItem, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description']


class ShoppingItemSerializer(serializers.ModelSerializer):
    product_name = ProductSerializer()
    class Meta:
        model = ShoppingItem
        fields = ["id", "created_at", "product_name", "location", "price", "amount"]
