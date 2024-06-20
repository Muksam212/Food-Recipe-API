from ..serializers.shoppinglist import ShoppingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from recipe.models import ShoppingList
from rest_framework.permissions import IsAuthenticated

class ShoppingList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingSerializer
    model = ShoppingList

    def get_queryset(self):
        return self.model.objects.all().filter(user = self.request.user)