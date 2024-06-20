from ..serializers.recipe import RecipeSerializer
from recipe.models import Recipe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ..views.filters import RecipeSetFilter
from django_filters.rest_framework import DjangoFilterBackend



class RecipeList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        recipes = Recipe.objects.filter(author = self.request.user)
        filtered_recipes = RecipeSetFilter(request.GET, queryset=recipes).qs
        serializer = RecipeSerializer(filtered_recipes, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        user = request.user
        recipe = Recipe.objects.filter(author = user)
        serializer = RecipeSerializer(recipe, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

class RecipeDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer
    lookup_field = "id"
    model = Recipe

    def get_queryset(self):
        return self.model.objects.all().filter(author = self.request.user)