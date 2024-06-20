from rest_framework import serializers
from recipe.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "user", "recipe", "rating")
        depth = 1