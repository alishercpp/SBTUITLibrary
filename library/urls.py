from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import (
    BookModelViewSet,
    OrderModelViewSet,
)

router = DefaultRouter()
router.register(r'books', BookModelViewSet)
router.register(r'orders', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
