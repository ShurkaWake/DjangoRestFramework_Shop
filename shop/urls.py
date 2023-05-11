from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    path('order/', include('shop.routing.order_urls')),
    path('category/', include('shop.routing.category_urls')),
    path('product/', include('shop.routing.product_urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
