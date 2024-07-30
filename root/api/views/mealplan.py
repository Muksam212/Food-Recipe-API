from ..serializers.mealplan import MealPlanSerializer
from recipe.models import MealPlan
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .filters import MealSetFilter

from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView

class MealPlanList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        meal_plan = MealPlan.objects.filter(user=self.request.user)
        filtered_recipes = MealSetFilter(request.GET, queryset=meal_plan).qs
        serializer = MealPlanSerializer(filtered_recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = MealPlanSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MealDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = MealPlanSerializer
    queryset = MealPlan.objects.all()
    lookup_field = "id"