from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet
from blog.views import OdamViewSet, IkonViewSet, SumpermisionViewSet, SponsrViewSet, MaqolaViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'odam', OdamViewSet)
router.register(r'ikon', IkonViewSet)
router.register(r'sumpermision', SumpermisionViewSet)
router.register(r'sponsr', SponsrViewSet)
router.register(r'maqolalar', MaqolaViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Maqola",
        default_version='v1',
        description="Test description",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="jamshidbek@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Fixed: Added trailing slash
    path('blog/', include('blog.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),  # Fixed: Added prefix for the API router
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
