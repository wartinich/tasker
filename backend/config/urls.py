from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="TASKER API",
      default_version='v1',
      description="TASKER API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #Apps
    path('api/v1/', include('tasks.urls')),
    path('api/v1/user/', include('users.urls')),

    #Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    #Swagger
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)