import requests
from django.test import TestCase
from vehicles.models import Manufacturer, Vehicle
from vehicles.serializers import EsVehicleSerializer
from indexer import es_api


class TestEsAPI(TestCase):
    def setUp(self):
        # Destroy any data after start application
        requests.delete(es_api.VEHICLE_BASE_URL)
        self.manufacturer = Manufacturer.objects.create(name='Fiat')
        self.vehicle = Vehicle.objects.create(
            manufacturer=self.manufacturer,
            model_name='Uno',
            engine='1000',
            color='vermelho',
            kms=1000
        )

    def test_indexacao(self):
        vehicle_data = EsVehicleSerializer(self.vehicle).data
        es_api.index_vehicle(vehicle_data)
        vehicle_es = es_api.get_vehicle(self.vehicle.id)
        self.assertEqual(vehicle_data, vehicle_es['_source'])

    def test_aggregation(self):
        self.test_indexacao()
        es_api.get_vehicle(self.vehicle.id)
        # O elasticsearch leva certo tempo para disponibilizar os documentos
        # na busca, é importante aguardar um tempo para poder realizar o test
        import time
        time.sleep(1)
        aggs = es_api.get_aggreagation('manufacturer.name')
        aggs_manufacturer = aggs['aggregations']['manufacturer.name']
        aggs_buckets = aggs_manufacturer['buckets']
        self.assertTrue(
            any(b['key'].lower() == 'fiat' for b in aggs_buckets)
        )
