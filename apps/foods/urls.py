from rest_framework.routers import DefaultRouter
from apps.foods.views import FoodAPIViewSet, FoodCategoryAPIViewSet


router = DefaultRouter()
router.register(r'food', FoodAPIViewSet, basename='foods')
router.register(r'foodcategory', FoodCategoryAPIViewSet, basename='foods-category')

urlpatterns = router.urls
