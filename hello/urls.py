from django.urls import path
from .views import products_cart, cart_clear, item_list, items_price_100, manage_item

urlpatterns = [
    #path('', HelloView.as_view(), name = 'index'),
    path("products_cart/", products_cart, name = "products_cart"),
    path("cart_clear/", cart_clear, name = "cart_clear"),

    #question 9
    path("items/", item_list, name = "item_list"),
    path("items/price100", items_price_100, name = "items_price_100"),

    path("items/manage", manage_item, name = "manage_items"),
]