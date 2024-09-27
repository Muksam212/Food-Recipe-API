from ..serializers.rating import RatingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Rating

from rest_framework.permissions import IsAuthenticated


class RatingList(ListCreateAPIView):
    serializer_class = RatingSerializer
    model = Rating
    queryset = Rating.objects.all()



class RatingDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    model = Rating
    queryset = Rating.objects.all()
    lookup_field = "id"