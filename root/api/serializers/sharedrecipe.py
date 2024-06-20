from rest_framework import serializers
from recipe.models import SharedRecipe

class SharedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedRecipe
        fields = (
            "id",
            "recipe",
            "shared_by",
            "shared_with",
            "shared_at"
        )