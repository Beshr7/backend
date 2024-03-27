
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("pressure_sensor.urls")),
    path("api2/", include("polls.urls")),
    path('', include(router.urls)),
]
