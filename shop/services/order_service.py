from ..models.order import Order
from ..serializers.order_serializer import Order_Serializer, Order_C_Serializer
from rest_framework import status
from rest_framework.response import Response

def get_order(order_id):
    instance = Order.objects.get(pk=order_id)
    order_serializer = Order_Serializer(instance)
    return Response(order_serializer.data, status.HTTP_200_OK)

def get_order_list():
    orders = Order.objects.all()
    serializer = Order_Serializer(orders, many = True)
    return Response(serializer.data, status.HTTP_200_OK)

def create_order(data):
    serializer = Order_C_Serializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def delete_order(order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_404_NOT_FOUND)
    
    try:
        order.delete()
    except:
        return Response({'message': 'Something went wrong'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_200_OK)