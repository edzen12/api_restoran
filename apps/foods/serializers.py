from rest_framework import serializers
from apps.foods.models import FoodCategory, Food


class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = ('id', 'main_title', 'title')


class FoodListSerializer(serializers.ModelSerializer):
    category = FoodCategorySerializer()

    class Meta:
        model = Food
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"
