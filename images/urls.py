from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageItemViewSet

router = DefaultRouter()
router.register('images', ImageItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]