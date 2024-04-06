from rest_framework import serializers
from .models import Pressure_Sensor, Pressure_Reading


class Pressure_Sensor_Serializers(serializers.ModelSerializer):
    latitude = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pressure_Sensor
        fields = ("id", "label", "installation_date", "latitude", "longitude")


class Pressure_Reading_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Pressure_Reading
        fields = ("id", "label", "date_time", "value", "sensor_id")
