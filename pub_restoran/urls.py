from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import api_root

schema_view = get_schema_view(
    openapi.Info(
        title="Pub Restoran",
        default_version='v1',
        description="API for Restoran",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nursultan.karagulov.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('', api_root, name='api-root'),
    path('foods/', include('apps.foods.urls')),
    path('departments/', include('apps.departmants.urls')),
]

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),

    # documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
