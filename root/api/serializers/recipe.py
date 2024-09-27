from rest_framework import serializers
from recipe.models import Recipe, Rating
from users.models import User

from django.db.models import Avg
from ..serializers.review import ReviewSerializer

class RecipeSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many = False)
    #it will count the number
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "description",
            "ingredients",
            "instructions",
            "author",
            "category",
            "average_rating"
        )

    #average count for rating
    def get_average_rating(self, obj):
        return obj.ratings.aggregate(Avg('rating'))['rating__avg']