from django.urls import path
from ..views.recipe import(
    RecipeList, 
    RecipeDetails
)

urlpatterns = [
    path('api/recipe/list/', RecipeList.as_view(), name = 'recipe-list'),
    path('api/recipe/update/<int:id>', RecipeDetails.as_view(), name = "recipe-update")
]
