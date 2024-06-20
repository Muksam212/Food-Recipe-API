from ..views.shoppinglist import (
    ShoppingList
)
from django.urls import path

urlpatterns = [
    path('api/shopping/list/', ShoppingList.as_view(), name = 'shopping-list')
]
