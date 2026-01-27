from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated

from vehicle.models import Car, Moto, Mileage
from vehicle.permisions import IsOwnerOrStaff
from vehicle.serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    """Представление для работы с автомобилями"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class MotoCreateAPIView(generics.CreateAPIView):
    """Создание нового мотоцикла"""
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


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
    permission_classes = [IsOwnerOrStaff]





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


class MileageListAPIView(generics.ListAPIView):
    """Получение списка всех пробегов"""
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('car', 'moto')  # Набор полей для фильтрации
    ordering_fields = ('year', )

