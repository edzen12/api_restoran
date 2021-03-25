from rest_framework import serializers
from apps.departmants.models import (
    Department,
    Booking,
    PhoneNumber,
)
from apps.foods.models import FoodCategory


class DepartmentFoodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    main_title = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)

    class Meta:
        model = FoodCategory
        fields = "__all__"


class PhoneNumberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    department = DepartmentFoodSerializer()

    class Meta:
        model = PhoneNumber
        fields = (
            'id', 'department',
            'number'
        )
        read_only_fields = ('department',)


class DepartmentListSerializer(serializers.ModelSerializer):
    food = DepartmentFoodSerializer(many=True, read_only=True)
    phone_number = PhoneNumberSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer(many=True, required=False)
    food = DepartmentFoodSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validated_data):
        phone_numbers = validated_data.pop('phone_number')
        foods = validated_data.pop('food')
        instance = Department.objects.create(**validated_data)
        for food in foods:
            try:
                food_obj = FoodCategory.objects.get(id=food.get('id'))
                instance.food.add(food_obj)
            except FoodCategory.DoesNotExist as error:
                raise serializers.ValidationError(error)
        for phone_number in phone_numbers:
            PhoneNumber.objects.create(department=instance, **phone_number)
        return instance

    def update(self, instance, validated_data):
        phone_numbers = validated_data.pop('phone_number', [])
        foods = validated_data.pop('food', [])
        for food in foods:
            try:
                food_obj = FoodCategory.objects.get(id=food.get('id'))
                instance.food.clear()
                instance.food.add(food_obj)
            except FoodCategory.DoesNotExist as error:
                raise serializers.ValidationError(error)
        for phone_number in phone_numbers:
            if phone_number.get('id') is None:
                phone_obj = PhoneNumber.objects.create(department=instance, **phone_number)
            else:
                phone_obj = PhoneNumber.objects.get(id=phone_number.get('id'))
                phone_obj.number = phone_number.get('number')
                phone_obj.save()
        return super().update(instance, validated_data)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'department', 'day', 'people',
            'number',
        )


class BookingListSerializer(serializers.ModelSerializer):
    department = DepartmentListSerializer()

    class Meta:
        model = Booking
        fields = "__all__"
