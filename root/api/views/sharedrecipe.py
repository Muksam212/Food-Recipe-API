from ..serializers.sharedrecipe import SharedRecipeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from recipe.models import SharedRecipe

class SharedRecipeList(ListCreateAPIView):
    serializer_class = SharedRecipeSerializer
    queryset = SharedRecipe.objects.all()
    model = SharedRecipe


class SharedRecipeDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = SharedRecipeSerializer
    queryset = SharedRecipe.objects.all()
    model = SharedRecipe
    lookup_field = "id"