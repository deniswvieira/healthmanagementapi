from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PatientViewSet

router = DefaultRouter()
router.register(r"patient", PatientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
