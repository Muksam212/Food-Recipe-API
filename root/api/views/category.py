from ..serializers.category import CategorySerializer
from recipe.models import Category

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from .filters import CategorySetFilter


#using function based views
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == "GET":
        queryset = Category.objects.all()
        filter_set = CategorySetFilter(request.GET, queryset = queryset)
        if filter_set.is_valid():
            queryset = filter_set.qs
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
        
    if request.method == "POST":
        serializer = CategorySerializer(data = request.data) #handle arbitary data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','PATCH','DELETE'])
def category_details(request, id = None):
    try:
        category = get_object_or_404(Category, id = id)
    except Category.DoesNotExist:
        return HttpResponse(status = 40)
    
    if request.method == "GET":
        serializer = get_object_or_404(category)
        return JsonResponse(serializer.data)
        
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "PATCH":
        serializer = CategorySerializer(category, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
