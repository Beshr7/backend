from django.urls import path
from django.views.generic import TemplateView
from .views import  Pressure_SensorView

# from . import views

app_name = "flowless"

urlpatterns = [

    path("pressure/", Pressure_SensorView, name="pressurereadingcreated"),
]
