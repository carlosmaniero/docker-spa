from rest_framework import serializers
from vehicles.models import Manufacturer, Vehicle


class ManufacturerSerializer(serializers.ModelSerializer):
    ''' Serializer of Manufacturer model'''

    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class VehicleSerializer(serializers.ModelSerializer):
    ''' Serializer of Vehicle model '''

    class Meta:
        model = Vehicle
        fields = [
            'id', 'manufacturer', 'model_name',
            'color', 'category', 'kms', 'engine'
        ]


class EsVehicleSerializer(VehicleSerializer):
    manufacturer = ManufacturerSerializer()
