from recipe.models import *
from django_filters import rest_framework as filters

class CategorySetFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ['slug']


class RecipeSetFilter(filters.FilterSet):
    author__name = filters.CharFilter(field_name = "author__name", lookup_expr="icontains")
    category__slug = filters.CharFilter(field_name = "category__slug", lookup_expr="icontains")
    category__name = filters.CharFilter(field_name = "category__name", lookup_expr="icontains")
    class Meta:
        model = Recipe
        fields = ["title", "author__name","category__slug", "category__name"]


class MealSetFilter(filters.FilterSet):
    name = filters.CharFilter(field_name = "user__name", lookup_expr="iexact")
    email = filters.CharFilter(field_name="user__email", lookup_expr="iexact")
    class Meta:
        model = MealPlan
        fields = ["name", "email"]


class UserSetFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ("email", "name")