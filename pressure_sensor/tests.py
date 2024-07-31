from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from pressure_sensor.views import Pressure_ReadingView
from rest_framework import status


class TestUrls(SimpleTestCase):
    def test_readings_url(self):
        url = reverse("pressurereadingcreated")
        self.assertEqual(resolve(url).func.view_class, Pressure_ReadingView)


class PressureReadingAggregationAPITest(TestCase):
    def test_until_after_since(self):
        since_date = "2024-05-10T00:00:00"
        until_date = "2024-05-12T00:00:00"
        url = reverse("pressurereadingcreated")
        data = {
            "since": since_date,
            "until": until_date,
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missing_query_parameters(self):
        url = reverse("pressurereadingcreated")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {"since": "2024-05-10T00:00:00"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {"until": "2024-05-12T00:00:00"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
