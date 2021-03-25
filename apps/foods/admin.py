from django.contrib import admin
from apps.foods.models import Food, FoodCategory

admin.site.register(Food)
admin.site.register(FoodCategory)
