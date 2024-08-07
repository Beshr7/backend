from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from datetime import datetime, date
from django.db.models import Model
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
try:
    from django.db.models import JSONField
except ImportError:
    # django < 3.1
    from django.contrib.postgres.fields import JSONField


class Pressure_Sensor(models.Model):
    label = models.CharField(max_length=200, default="default")
    installation_date = models.DateTimeField("installation date")
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    serial_number = models.CharField(max_length=200, unique=True)
    configuration = JSONField(default=dict, blank=True, null=True)

    def clean(self):
        super().clean()
        if not self.label.startswith("PSSR"):
            raise ValidationError("Pressure sensor label must start with 'PSSR'.")

    def __str__(self):
        return self.label


class Pressure_Reading(models.Model):
    label = models.CharField(max_length=200, default="default")
    date_time = models.DateTimeField("installation date")
    value = models.FloatField(default=0.00)
    row_value = models.FloatField(default=0.00)
    sensor_id = models.ForeignKey(
        "Pressure_Sensor",
        verbose_name="Sensor ID",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label
