from rest_framework import viewsets
from vehicles.models import Manufacturer, Vehicle
from vehicles.serializers import ManufacturerSerializer, VehicleSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
