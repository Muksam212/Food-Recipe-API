from ..views.category import category_list
from django.urls import path

urlpatterns = [
    path('api/category/list/', category_list, name = "category-list"),
]
