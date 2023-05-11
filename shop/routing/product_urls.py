from django.urls import path
from ..views.product_view import *

urlpatterns = [
    path('<int:product_id>', product_rud),
    path('', product_create_and_list),
]
