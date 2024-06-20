from rest_framework import serializers
from recipe.models import Category

from ..serializers.recipe import RecipeSerializer

class CategorySerializer(serializers.ModelSerializer):
    #nested serializer
    # recipes = RecipeSerializer(many = True)
    class Meta:
        model = Category
        fields = ("id","name", "slug")