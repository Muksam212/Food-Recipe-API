from ..serializers.rating import RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Rating

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class RatingList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        rating = Rating.objects.all().filter(user = user)
        serializer = RatingSerializer(rating, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = RatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        


class RatingDetails(APIView):
    def get(self, request, id = None):
        rating = get_object_or_404(Rating, id = id)
        serializer = RatingSerializer(rating, many = False)
        return Response(serializer.data)

    def put(self, request, id = None):
        rating = get_object_or_404(Rating, id = id)
        serializer = RatingSerializer(rating, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_200_OK)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, id = None):
        rating = get_object_or_404(Rating, id = id)
        serializer = RatingSerializer(rating, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_200_OK)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)