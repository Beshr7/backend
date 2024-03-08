from django.http import HttpResponse
from django.shortcuts import render
from .models import Pressure_Sensor
# Create your views here.

def Pressure_SensorView(request):
    Pressure_Sensors =Pressure_Sensor.objects.all()

    return HttpResponse(Pressure_Sensors)