from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
