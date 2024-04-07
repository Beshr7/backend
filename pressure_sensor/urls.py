from django.urls import path, include
from .views import PressureSensorViewSet, PressureSensorViewSet2, Pressure_ReadingView, Pressure_SensorHTTPView
from rest_framework import routers


router = routers.DefaultRouter()

# this is for viewset
router.register(r'pressure-viewset', PressureSensorViewSet2, basename='user')

urlpatterns = [
    path("pressure-generic/", PressureSensorViewSet.as_view({'get': 'list'})    , name="pressuresensorhttpcreated"),
    path("pressure-HTTP/", Pressure_SensorHTTPView, name="pressuresensorhttpcreated"),
    path("readings/", Pressure_ReadingView.as_view(), name="pressurereadingcreated"),
]

urlpatterns += router.urls