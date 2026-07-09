from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Sensor, Measurement

class SensorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sensor_data = {
            'name': 'ESP32',
            'description': 'Датчик на кухне'
        }
        self.sensor = Sensor.objects.create(**self.sensor_data)

    def test_create_sensor(self):
        """Тест создания датчика"""
        url = reverse('sensor-list')
        response = self.client.post(url, self.sensor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sensor.objects.count(), 2)  # один уже создан в setUp

    def test_get_sensors_list(self):
        """Тест получения списка датчиков"""
        url = reverse('sensor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_sensor_detail(self):
        """Тест получения детальной информации о датчике"""
        url = reverse('sensor-detail', args=[self.sensor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.sensor.name)

    def test_update_sensor(self):
        """Тест обновления датчика"""
        url = reverse('sensor-detail', args=[self.sensor.id])
        updated_data = {'description': 'Перенесён на балкон'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sensor.refresh_from_db()
        self.assertEqual(self.sensor.description, 'Перенесён на балкон')

    def test_create_measurement(self):
        """Тест создания измерения"""
        url = reverse('measurement-create')
        measurement_data = {
            'sensor': self.sensor.id,
            'temperature': 24.5
        }
        response = self.client.post(url, measurement_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Measurement.objects.count(), 1)