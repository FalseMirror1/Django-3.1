# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(ListCreateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class SensorUpdateView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()


class MeasurementPlusView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()