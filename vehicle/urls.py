from os import path

from django.urls import include, path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MileageCreateAPIView, MotoMileageListAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto-retrieve'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto-destroy'),
    # mileage
    path('mileage/create/', MileageCreateAPIView.as_view(), name='mileage-create'),
    path('moto/mileage/', MotoMileageListAPIView.as_view(), name='moto-mileage'),
] + router.urls