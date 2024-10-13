from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryModelViewSet,
    ProductModelViewSet,
    SalesmanAdditionallyModelViewSet,
    SalesmanModelViewSet,
    index,
)


router = DefaultRouter()
router.register("", ProductModelViewSet)
router.register("categories", CategoryModelViewSet)
router.register("salesman", SalesmanModelViewSet)
router.register("salesman_additionally", SalesmanAdditionallyModelViewSet)


urlpatterns = [
    path("index/", index),
    path("", include(router.urls)),
]
