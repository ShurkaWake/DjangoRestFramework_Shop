from ..models import Category
from ..serializers.category_serializer import Category_Serializer
from rest_framework import status
from rest_framework.response import Response

def get_categories_list():
    categories = Category.objects.all()
    serializer = Category_Serializer(categories, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

def get_category(category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    serializer = Category_Serializer(category)
    return Response(serializer.data, status.HTTP_200_OK)

def create_category(data):
    serializer = Category_Serializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_category(category_id, data):
    try:
        category = Category.objects.get(pk=category_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    serializer = Category_Serializer(category, data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_category(category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    try:
        category.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_200_OK)