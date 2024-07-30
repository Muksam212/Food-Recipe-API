from ..serializers.category import CategorySerializer
from recipe.models import Category

from .filters import *

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    search_fields = ["slug"]
    filter_backends = [DjangoFilterBackend]
    model = Category
    queryset = Category.objects.all()


class CategoryDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    model = Category
    lookup_field = "slug"
    queryset = Category.objects.all()