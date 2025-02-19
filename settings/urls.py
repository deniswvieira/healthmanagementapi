from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="HEALTH MANAGEMENT FHIR API",
        default_version="v1",
        description="Health Management FHIR compliant API",
        contact=openapi.Contact(email="deniswvieira@gmail.com"),
        license=openapi.License(name="Proprietary License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("", include("apps.portal.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("fhir/", include("apps.patients.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
