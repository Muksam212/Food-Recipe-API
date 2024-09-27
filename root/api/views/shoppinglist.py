from ..serializers.shoppinglist import ShoppingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from recipe.models import ShoppingList
from rest_framework.permissions import IsAuthenticated

class ShoppingList(ListCreateAPIView):
    serializer_class = ShoppingSerializer
    model = ShoppingList
    queryset = ShoppingList.objects.all()