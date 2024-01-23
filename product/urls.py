from django.urls import path
from product.views import main_view, product_view, products_view, product_list_view, shopping_list_view, Shoppinglist

urlpatterns = [
    path("", main_view),
    path("product/", products_view),
    path("product/<int:resource_id>", product_view),
    path("product_list/", product_list_view),
    path("shopping_list/", shopping_list_view),
    path('shopping_list_api/', Shoppinglist.as_view()),
    path('shopping_list_api/<int:resource_id>', Shoppinglist.as_view()),
]
