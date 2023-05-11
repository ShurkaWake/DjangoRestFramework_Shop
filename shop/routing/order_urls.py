from django.urls import path
from ..views.order_view import order, get_order

urlpatterns = [
    path('<int:order_id>', get_order),
    path('', order),
]
