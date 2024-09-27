from ..serializers.review import ReviewSerializer
from recipe.models import Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    model = Review

class ReviewDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    model = Review
    lookup_field = "id"