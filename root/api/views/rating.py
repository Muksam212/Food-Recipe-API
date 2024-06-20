from ..serializers.rating import RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Rating

class RatingList(APIView):
    def get(self, request):
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = RatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
