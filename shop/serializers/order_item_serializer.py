from rest_framework import serializers
from .product_serializer import Product_Serializer
from ..models.order_item import Order_Item
from ..models.order import Order
from ..models.product import Product

class Order_Item_Serializer(serializers.ModelSerializer):
    product = Product_Serializer()

    class Meta:
        model = Order_Item
        fields = [
            'id',
            'product',
            'quantity',
        ]

class Order_Item_C_Serializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Order_Item
        fields = [
            'product_id',
            'quantity',
        ]

    def create(self, validated_data):
        return Order_Item.objects.create(
            product = validated_data.get('product_id'),
            quantity = validated_data.get('quantity'),
        )
