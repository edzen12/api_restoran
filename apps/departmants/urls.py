from rest_framework.routers import DefaultRouter
from apps.departmants.views import (
    DepartmentAPIViewSet,
    BookingAPIViewSet,
)


router = DefaultRouter()
router.register(r'departments', DepartmentAPIViewSet, basename='departments')
router.register(r'bookings', BookingAPIViewSet, basename='bookings')

urlpatterns = router.urls
