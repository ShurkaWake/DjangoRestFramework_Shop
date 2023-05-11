from ..models import Product
from ..serializers.product_serializer import Product_Serializer, Product_CU_Serializer
from rest_framework import status
from rest_framework.response import Response

def get_products_list():
    products = Product.objects.all()
    serializer = Product_Serializer(products, many = True)
    return Response(serializer.data, status.HTTP_200_OK)

def get_product(product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    serializer = Product_Serializer(product)
    return Response(serializer.data, status.HTTP_200_OK)

def create_product(data):
    serializer = Product_CU_Serializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def update_product(product_id, data):
    try:
        product = Product.objects.get(pk=product_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    serializer = Product_CU_Serializer(product, data)
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_product(product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    try:
        product.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_200_OK)