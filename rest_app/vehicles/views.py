from rest_framework import viewsets
from vehicles.models import Manufacturer
from vehicles.serializers import ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
