from rest_framework import serializers
from vehicles.models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    ''' Serializer of Manufacturer model'''

    class Meta:
        model = Manufacturer
