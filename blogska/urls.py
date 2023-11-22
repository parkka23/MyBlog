"""blogska URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# from drf_yasg import openapi
# from rest_framework.schemas import get_schema_view


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Your API",
#       default_version='v1',
#       description="Your API description",
#       terms_of_service="https://www.example.com/terms/",
#       contact=openapi.Contact(email="contact@example.com"),
#       license=openapi.License(name="Your License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),

# Define Swagger UI and JSON views
#     path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Optionally add Redoc

] + i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),  # ml
    path('', include('blog.urls')),
    path('', include('users.urls')),
    prefix_default_language=False
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
