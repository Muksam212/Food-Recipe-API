from django.urls import path
from ..views.mealplan import(
    MealPlanList
)
urlpatterns = [
    path('api/meal/plan/list/', MealPlanList.as_view(), name = 'meal-plan')
]
