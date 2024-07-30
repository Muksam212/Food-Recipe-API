from django.urls import path

from ..views.category import CategoryList, CategoryDetails

urlpatterns = [
    path('api/category/list/', CategoryList.as_view(), name = "category-list"),
    path('api/category/details/<slug:slug>/', CategoryDetails.as_view(), name = 'category-details')
]
