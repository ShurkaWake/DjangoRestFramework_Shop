from django.http import JsonResponse
from rest_framework.decorators import api_view
from ..services.category_service import *
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def category_create_and_list(request):
    if request.method == 'GET':
        return get_categories_list()
    elif request.method == 'POST':
        return create_category(JSONParser().parse(request))

@api_view(['GET', 'PUT', 'DELETE'])
def category_rud(request, category_id):
    if request.method == 'GET':
        return get_category(category_id)
    elif request.method == 'PUT':
        return update_category(category_id, JSONParser().parse(request))
    elif request.method == 'DELETE':
        return delete_category(category_id)