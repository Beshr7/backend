from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Pressure_Sensor, Pressure_Reading
from .serializers import Pressure_Sensor_Serializers, Pressure_Reading_Serializers
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PressureReadingFilterSet
from rest_framework import viewsets
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class PressureSensorViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Pressure_Sensor.objects.all()
    serializer_class = Pressure_Sensor_Serializers






class PressureSensorViewSet2(viewsets.ViewSet):


    def list(self, request):
        queryset = Pressure_Sensor.objects.all()
        serializer = Pressure_Sensor_Serializers(queryset, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def create(self, request):
        serializer = Pressure_Sensor_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({})


def Pressure_SensorHTTPView(request):
    Pressure_Sensors = Pressure_Sensor.objects.all()

    return HttpResponse(Pressure_Sensors)


class Pressure_ReadingView(generics.ListCreateAPIView):

    # def Reading_Filter():
    #     filtered_readings = []
    #     from_date = timezone.make_aware(datetime(2020, 1, 1), timezone=timezone.utc)
    #     to_date = timezone.make_aware(datetime(2020, 12, 31), timezone=timezone.utc)
    #     for reading in Pressure_Reading.objects.all():
    #         if from_date < reading.date_time < to_date:
    #             filtered_readings.append(reading)

    #     return filtered_readings
    serializer_class = Pressure_Reading_Serializers
    queryset = Pressure_Reading.objects.all()

    # def get(self, request, format=None):
    #     labeltest = request.query_params.get("label")
    #     if labeltest:
    #         readings = Pressure_Reading.objects.all().filter(label=labeltest)
    #     else:
    #         readings = Pressure_Reading.objects.all()

    #     data = {"pressure readings": list(readings.values())}

    #     return Response(data)

    # to add filter button in api page
    filter_backends = [DjangoFilterBackend]
    filterset_class = PressureReadingFilterSet

    def get(self, request, *args, **kwargs):
        logger.info("Pressure_ReadingView: GET request received")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info("Pressure_ReadingView: POST request received with data %s", request.data)
        return super().post(request, *args, **kwargs)
