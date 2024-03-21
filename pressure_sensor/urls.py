from django.urls import path, include
from .views import PressureSensorViewSet, Pressure_ReadingView, Pressure_SensorHTTPView
from rest_framework import routers

app_name = "flowless"
router = routers.SimpleRouter()


router.register(r'pressure', PressureSensorViewSet, basename='user')

urlpatterns = [
    # Your other URL patterns
    # path('pressure', PressureSensorViewSet),
    path("pressure-HTTP/", Pressure_SensorHTTPView, name="pressuresensorhttpcreated"),
    path("readings/", Pressure_ReadingView.as_view(), name="pressurereadingcreated"),
]

urlpatterns += router.urls