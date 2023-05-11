from rest_framework.decorators import api_view
from ..services.product_service import *
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def product_create_and_list(request):
    if request.method == 'GET':
        return get_products_list()
    elif request.method == 'POST':
        return create_product(JSONParser().parse(request))

@api_view(['GET', 'PUT', 'DELETE'])
def product_rud(request, product_id):
    if request.method == 'GET':
        return get_product(product_id)
    elif request.method == 'PUT':
        return update_product(product_id, JSONParser().parse(request))
    elif request.method == 'DELETE':
        return delete_product(product_id)