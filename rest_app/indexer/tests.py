import requests
import time
import socket
from django.conf import settings
from django.test import TestCase
from vehicles.models import Manufacturer, Vehicle
from vehicles.serializers import EsVehicleSerializer
from indexer import es_api
from indexer.models import IndexModel
from datetime import datetime


class TestEsAPI(TestCase):
    _socket = None

    def setUp(self):
        if not self._socket:
            self._socket = socket.socket
        self.enable_conection()
        # Wait for elasticsearch
        for i in range(10):
            try:
                response = requests.get(settings.ELASTICSEARCH_HOST)
            except Exception as e:
                time.sleep(2)
            else:
                if response.status_code == 200:
                    break

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

    def block_connection(self):
        def _socket(*args, **kargs):
            raise Exception('Keep Out!')
        socket.socket = _socket

    def enable_conection(self):
        socket.socket = self._socket

    def test_index_vehicle(self):
        vehicle_data = EsVehicleSerializer(self.vehicle).data
        es_api.index_vehicle(vehicle_data)
        vehicle_es = es_api.get_vehicle(self.vehicle.id)
        self.assertEqual(vehicle_data, vehicle_es['_source'])

    def test_get_vehicle_exceptions(self):
        with self.assertRaises(es_api.ESIndexException):
            es_api.get_vehicle('sdsaoidjas;/asd;asd-asd90as9d/asd')

    def test_index_vehicle_exception(self):
        self.test_index_vehicle()
        with self.assertRaises(es_api.ESIndexException):
            es_api.index_vehicle({'id': 'another-thing', 'message': 'foobar'})

    def test_aggregation(self):
        self.test_index_vehicle()
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

        with self.assertRaises(es_api.ESIndexException):
            es_api.get_aggreagation('>>>>:::<<<manufacture{}ASDr.name&&¨*&%')

    def test_connectivity_exception(self):
        self.block_connection()
        with self.assertRaises(es_api.ESConnectionProblem):
            reponse = es_api.get_vehicle(1)
        self.block_connection()
        with self.assertRaises(es_api.ESConnectionProblem):
            self.test_index_vehicle()
        self.block_connection()
        with self.assertRaises(es_api.ESConnectionProblem):
            es_api.get_aggreagation('manufacturer.name')
        self.enable_conection()

    def test_index_mode_update(self):
        index = IndexModel()
        self.assertEqual(index.indexed_at, None)

        before_update = datetime.now()
        index.update_index_time(False)
        self.assertGreaterEqual(index.indexed_at, before_update)

        before_update = datetime.now()
        with self.assertRaises(Exception):
            # This is a abstract class
            index.update_index_time(True)
        self.assertGreaterEqual(index.indexed_at, before_update)
