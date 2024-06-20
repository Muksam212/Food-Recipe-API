from rest_framework import serializers
from recipe.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user", "recipe", "review")