from ..serializers.recipe import RecipeSerializer
from recipe.models import Recipe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ..views.filters import RecipeSetFilter
from django_filters.rest_framework import DjangoFilterBackend



class RecipeList(ListCreateAPIView):
    serializer_class = RecipeSerializer
    model = Recipe
    queryset = Recipe.objects.all()


class RecipeDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    lookup_field = "id"
    model = Recipe
    queryset = Recipe.objects.all()