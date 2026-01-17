from rest_framework import viewsets

from vehicle.models import Car
from vehicle.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
