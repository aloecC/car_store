from os import path

from django.urls import include, path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    # твои маршруты могут быть добавлены здесь
] + router.urls