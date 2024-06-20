from recipe.models import *
from django_filters import rest_framework as filters

class CategorySetFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class RecipeSetFilter(filters.FilterSet):
    author__name = filters.CharFilter(field_name = "author__name", lookup_expr="icontains")
    category__slug = filters.CharFilter(field_name = "category__slug", lookup_expr="icontains")
    category__name = filters.CharFilter(field_name = "category__name", lookup_expr="icontains")
    class Meta:
        model = Recipe
        fields = ["title", "author__name","category__slug", "category__name"]


class MealSetFilter(filters.FilterSet):
    user__name = filters.CharFilter(field_name = "user__name", lookup_expr="icontains")
    class Meta:
        model = MealPlan
        fields = ["user__name"]