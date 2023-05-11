from rest_framework import serializers
from ..models.order import Order
from ..models.order_item import Order_Item
from .user_serializer import User_Serializer
from django.contrib.auth.models import User
from .order_item_serializer import Order_Item_Serializer, Order_Item_C_Serializer

class Order_Serializer(serializers.ModelSerializer):
    user = User_Serializer()
    order_items = Order_Item_Serializer(source='get_order_items', many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'order_items',
            'order_date',
        ]

class Order_C_Serializer(serializers.ModelSerializer):
    order_items = Order_Item_C_Serializer(many=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = [
            'user_id',
            'order_items',
        ]

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(
            user = validated_data.get('user_id')
        )
        for item in order_items:
            Order_Item.objects.create(
                order = order,
                product = item.get('product_id'),
                quantity = item.get('quantity')
            )
        return order
