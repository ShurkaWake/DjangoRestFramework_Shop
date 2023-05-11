from django.urls import path
from ..views.category_view import *

urlpatterns = [
    path('<int:category_id>', category_rud),
    path('', category_create_and_list),
]
