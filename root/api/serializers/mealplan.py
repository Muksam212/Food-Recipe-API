from rest_framework import serializers
from recipe.models import MealPlan, Recipe

class MealPlanSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(queryset = Recipe.objects.all(), many  = True)
    class Meta:
        model = MealPlan
        fields = ("id","user", "date", "recipes")