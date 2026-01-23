from rest_framework import viewsets, generics

from vehicle.models import Car, Moto, Mileage
from vehicle.serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    """Представление для работы с автомобилями"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotoCreateAPIView(generics.CreateAPIView):
    """Создание нового мотоцикла"""
    serializer_class = MotoCreateSerializer


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    """Получение информации о конкретном мотоцикле"""
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoListAPIView(generics.ListAPIView):
    """Получение списка всех мотоциклов"""
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о конкретном мотоцикле"""
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    """Удаление конкретного мотоцикла"""
    queryset = Moto.objects.all()


class MileageCreateAPIView(generics.CreateAPIView):
    """Создание записи о пробеге для автомобиля или мотоцикла"""
    serializer_class = MileageSerializer


class MotoMileageListAPIView(generics.ListAPIView):
    """Получение списка всех пробегов мотоциклов"""
    queryset = Mileage.objects.filter(moto__isnull=False)
    serializer_class = MotoMileageSerializer

