from rest_framework import serializers
from .category_serializer import Category_Serializer
from ..models.product import Product
from ..models.category import Category

class Product_Serializer(serializers.ModelSerializer):
    category = Category_Serializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'category',
        ]

class Product_CU_Serializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many = False)

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'category_id',
        ]

    def create(self, validated_data):
        return Product.objects.create(
            name=validated_data.get('name'),
            price=validated_data.get('price'),
            category=validated_data.get('category_id')
        )
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.price=validated_data.get('price', instance.price)
        instance.category=validated_data.get('category_id', instance.category)
        instance.save()
        return instance