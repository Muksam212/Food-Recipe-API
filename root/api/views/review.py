from ..serializers.review import ReviewSerializer
from recipe.models import Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class ReviewList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    model = Review

    def get_queryset(self):
        return self.model.objects.all().filter(user = self.request.user)
    

class ReviewDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    model = Review
    lookup_field = "id"

    def get_queryset(self):
        return self.model.objects.all().filter(user = self.request.user)