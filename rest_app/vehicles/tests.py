from rest_framework.test import APITestCase
from rest_framework import status
from vehicles.models import Manufacturer, Vehicle


class ManufacturerTest(APITestCase):
    def setUp(self):
        Manufacturer.objects.all().delete()
        self.api_base = '/api/manufacturers/'

    def test_empty_list(self):
        response = self.client.get(self.api_base, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_get_one(self):
        manufacturer = Manufacturer.objects.create(name='GM')
        manufacturer_json = {
            'id': manufacturer.id,
            'name': manufacturer.name,
        }

        response = self.client.get(self.api_base, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [manufacturer_json])

        response = self.client.get(
            '{}{}/'.format(self.api_base, manufacturer.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), manufacturer_json)

    def test_put(self):
        manufacturer, _ = Manufacturer.objects.get_or_create(name='GM')
        response = self.client.put(
            '{}{}/'.format(self.api_base, manufacturer.pk),
            data={'name': 'Chevrolet'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            '{}{}/'.format(self.api_base, manufacturer.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Chevrolet')

    def test_post(self):
        response = self.client.post(self.api_base, data={
            'name': 'Fiat'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        fiat = Manufacturer.objects.filter(name='Fiat')

        self.assertEqual(fiat.count(), 1)

    def test_delete(self):
        fiat, _ = Manufacturer.objects.get_or_create(name='Fiat')

        response = self.client.delete(
            '{}{}/'.format(self.api_base, fiat.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        fiat = Manufacturer.objects.filter(name='Fiat')

        self.assertEqual(fiat.count(), 0)


class VehicleTest(APITestCase):
    def setUp(self):
        Manufacturer.objects.all().delete()
        Vehicle.objects.all().delete()
        self.api_base = '/api/vehicles/'

    def test_empty_list(self):
        response = self.client.get(self.api_base, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_get_one(self):
        manufacturer = Manufacturer.objects.create(name='GM')
        manufacturer_json = {
            'id': manufacturer.id,
            'name': manufacturer.name,
        }
        # Sorry, não conheço muito de carro.
        vehicle = Vehicle.objects.create(
            manufacturer=manufacturer,
            model_name='Vectra',
            color='prata',
            category='carro',
            kms=10,
            engine='v8'
        )
        vehicle_json = {
            'id': vehicle.id,
            'manufacturer': manufacturer.id,
            'model_name': vehicle.model_name,
            'color': vehicle.color,
            'category': vehicle.category,
            'kms': vehicle.kms,
            'engine': vehicle.engine
        }

        response = self.client.get(self.api_base, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [vehicle_json])

        response = self.client.get(
            '{}{}/'.format(self.api_base, vehicle.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), vehicle_json)

    def test_put(self):
        manufacturer = Manufacturer.objects.create(name='GM')
        vehicle = Vehicle.objects.create(
            manufacturer=manufacturer,
            model_name='Vectra',
            color='prata',
            category='carro',
            kms=10,
            engine='v8'
        )

        manufacturer, _ = Manufacturer.objects.get_or_create(
            name='Chevrolet'
        )

        response_get = self.client.get(
            '{}{}/'.format(self.api_base, vehicle.pk),
            format='json'
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        vehicle_json = response_get.json()
        vehicle_json['model_name'] = 'Opala'
        vehicle_json['manufacturer'] = manufacturer.id

        response = self.client.put(
            '{}{}/'.format(self.api_base, vehicle.pk),
            data=vehicle_json,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            '{}{}/'.format(self.api_base, vehicle.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['model_name'], 'Opala')
        self.assertEqual(
            response.json()['manufacturer'],
            manufacturer.id
        )

    def test_post(self):
        response = self.client.post('/api/manufacturers/', data={
            'name': 'Fiat'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        fiat_id = response.json()['id']
        vehicle_json = {
            'manufacturer': fiat_id,
            'model_name': 'Uno',
            'color': 'vermelho',
            'category': 'carro',
            'kms': 42,
            'engine': '1000'
        }
        response = self.client.post(self.api_base, data=vehicle_json)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vehicle_json['manufacturer_id'] = vehicle_json['manufacturer']
        del vehicle_json['manufacturer']

        vehicles = Vehicle.objects.filter(**vehicle_json)
        self.assertEqual(vehicles.count(), 1)

    def test_delete(self):
        fiat = Manufacturer.objects.create(name='fiat')
        vehicle_json = {
            'manufacturer_id': fiat.id,
            'model_name': 'Uno',
            'color': 'vermelho',
            'category': 'carro',
            'kms': 42,
            'engine': '1000'
        }
        vehicle = Vehicle.objects.create(**vehicle_json)
        response = self.client.delete(
            '{}{}/'.format(self.api_base, vehicle.pk),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Vehicle.objects.filter(**vehicle_json).count(),
            0
        )
