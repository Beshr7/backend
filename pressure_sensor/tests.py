from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from pressure_sensor.views import Pressure_ReadingView


class TestUrls(SimpleTestCase):
    def test_readings_url(self):
        url = reverse("pressurereadingcreated")
        self.assertEqual(resolve(url).func.view_class, Pressure_ReadingView)
