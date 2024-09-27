from ..serializers.mealplan import MealPlanSerializer
from recipe.models import MealPlan
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .filters import MealSetFilter


from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class MealPlanList(ListCreateAPIView):
    serializer_class = MealPlanSerializer
    model = MealPlan
    queryset = MealPlan.objects.all()


class MealDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = MealPlanSerializer
    queryset = MealPlan.objects.all()
    lookup_field = "id"