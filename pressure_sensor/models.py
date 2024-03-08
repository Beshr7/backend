from django.db import models
from datetime import datetime, date
from django.utils.dateparse import parse_date


class Pressure_Sensor(models.Model):
    label = models.CharField(max_length=200, default="default")
    installation_date = models.DateTimeField(
        "installation date", default=datetime.now()
    )
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    serial_number = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.label


class Pressure_Reading(models.Model):
    label = models.CharField(max_length=200, default="default")
    date_time = models.DateTimeField("installation date", default=datetime.now())
    value = models.FloatField(default=0.00)
    sensor_id = models.ForeignKey(
        "Pressure_Sensor",
        verbose_name="Sensor ID",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label
