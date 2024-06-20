from ..views.sharedrecipe import (
    SharedRecipeList,
    SharedRecipeDetails
)
from django.urls import path, include

urlpatterns = [
    path('api/shared/recipe/list/', SharedRecipeList.as_view(), name = 'shared-recipe'),
    path('api/shared/recipe/update/<int:id>/', SharedRecipeDetails.as_view(), name = 'shared-recipe-update')
]
