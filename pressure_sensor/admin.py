from django.contrib import admin
from .models import Pressure_Sensor,Pressure_Reading
import random
import string
from.forms import PressureSensorForm

class Pressure_Sensor_Class(admin.ModelAdmin):
    list_display = ("id", "label", "installation_date", "latitude", "longitude")
    readonly_fields = ["serial_number"]
    form = PressureSensorForm

    def save_model(self, *args, **kwargs):
        if not self.serial_number:
            # Generate a random string
            self.serial_number = "".join(
                random.choices(string.ascii_letters + string.digits, k=10)
            )
            # Ensure the generated code is unique
            while Pressure_Sensor.objects.filter(
                serial_number=self.serial_number
            ).exists():
                self.serial_number = "".join(
                    random.choices(string.ascii_letters + string.digits, k=10)
                )
        super(Pressure_Sensor, self).save(*args, **kwargs)


admin.site.register(Pressure_Sensor, Pressure_Sensor_Class)

admin.site.register(Pressure_Reading)