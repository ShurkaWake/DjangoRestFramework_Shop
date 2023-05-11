from django.urls import path
from ..views.order_view import order, order_noparam

urlpatterns = [
    path('<int:order_id>', order_noparam),
    path('', order),
]
