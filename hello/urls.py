from django.urls import path
from .views import products_cart, cart_clear

urlpatterns = [
    #path('', HelloView.as_view(), name = 'index'),
    path("products_cart/", products_cart, name = "products_cart"),
    path("cart_clear/", cart_clear, name = "cart_clear"),
]