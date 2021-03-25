from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.foods.serializers import FoodListSerializer
from apps.departmants.models import (
    Department,
    Booking,
)
from apps.foods.models import Food
from apps.departmants.serializers import (
    DepartmentListSerializer,
    DepartmentSerializer,
    BookingListSerializer,
    BookingSerializer,
)


class DepartmentAPIViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.prefetch_related('food', 'phone_number').all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=['get'])
    def foods(self, request, pk=None):
        departments = self.get_object()
        food = Food.objects.filter(category__in=departments.food.all())
        if food is not None:
            serializer = FoodListSerializer(food, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def booking(self, request, pk=None):
        departments = self.get_object()
        booking = departments.booking.all()
        if booking is not None:
            serializer = BookingListSerializer(booking, many=True)
            return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DepartmentListSerializer
        return DepartmentSerializer


class BookingAPIViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookingListSerializer
        return BookingSerializer
