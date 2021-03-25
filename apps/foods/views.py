from rest_framework import viewsets
from apps.foods.models import FoodCategory, Food
from apps.foods.serializers import (
    FoodCategorySerializer,
    FoodSerializer,
    FoodListSerializer,
)


class FoodAPIViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return FoodListSerializer
        return self.serializer_class


class FoodCategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
