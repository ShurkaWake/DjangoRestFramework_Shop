from rest_framework import serializers
from ..models.category import Category

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]