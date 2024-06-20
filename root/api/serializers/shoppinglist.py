from rest_framework import serializers
from recipe.models import ShoppingList

class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = (
            "id",
            "user",
            "recipes"
        )