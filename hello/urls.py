from django.urls import path
from .views import products_cart, cart_clear, item_list, items_price_100, \
    manage_item, edit_item, item_edit_list, search_item_by_name, search_item_by_price, \
    sort_items_by_price, count_items

urlpatterns = [
    #path('', HelloView.as_view(), name = 'index'),
    path("products_cart/", products_cart, name = "products_cart"),
    path("cart_clear/", cart_clear, name = "cart_clear"),

    #question 9
    path("items/", item_list, name = "item_list"),
    path("items/price100", items_price_100, name = "items_price_100"),

    #question 10
    path("items/manage", manage_item, name = "manage_item"),
    path("items/edit/", item_edit_list, name = "item_edit_list"),
    path("items/edit/<int:item_id>/", edit_item, name = "edit_item"),

    #question 11
    path("items/search_name/", search_item_by_name, name = "search_item_by_name"),
    path("items/search_price/", search_item_by_price, name = "search_item_by_price"),

    #question 12
    path("items/sorted_price/", sort_items_by_price, name = "sort_items_by_price"),
    path("items/list_with_count/", count_items, name = "count_items"),
]