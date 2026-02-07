from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):

    def SetUp(self) -> None:
        pass

    def test_create_car(self):
        '''Тестирование создание машины'''
        data = {
            'title': 'Test',
            'description': 'Test'
        }
        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'last_mileage': None, 'mileage': [], 'title': 'Test', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """Тестирование вывода списка машин"""

        Car.objects.create(
            title='list test',
            description='list test'
        )
        response = self.client.get('/cars/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем, что ответ является списком
        self.assertIsInstance(response.json(), list)

        # Проверяем, что в списке есть ожидаемый объект
        self.assertEqual(
            len(response.json()), 1  # Убедитесь, что в списке один элемент
        )

        expected_car = {
            'id': 2,
            'last_mileage': None,
            'mileage': [],
            'title': 'list test',
            'description': 'list test',
            'owner': None
        }

        self.assertEqual(
            response.json()[0],  # Проверяем первый элемент списка
            expected_car
        )