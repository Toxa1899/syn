from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryModelViewSet,
    ProductModelViewSet,
    SalesmanAdditionallyModelViewSet,
    SalesmanModelViewSet,
)


router = DefaultRouter()
router.register("categories", CategoryModelViewSet)
router.register("salesman", SalesmanModelViewSet)
router.register("salesman_additionally", SalesmanAdditionallyModelViewSet)
router.register("", ProductModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
