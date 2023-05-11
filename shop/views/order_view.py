from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from ..models.order import Order
from ..serializers.order_serializer import Order_Serializer
from ..services.order_service import *

# Create your views here.

@api_view(['GET', 'DELETE'])
def get_order(request, order_id):
    if request.method == 'GET':
        return get_order(order_id)
    elif request.method == 'DELETE':
        return delete_order(order_id)


@api_view(['GET', 'POST'])
def order(request):
    if request.method == 'GET':
        return get_order_list()
    elif request.method == 'POST':
        return create_order(JSONParser().parse(request))
