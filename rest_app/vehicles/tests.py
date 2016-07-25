from rest_framework.test import APITestCase
from rest_framework import status
from vehicles.models import Manufacturer, Vehicle


class ManufacturerTest(APITestCase):
    def setUp(self):
        Manufacturer.objects.all().delete()
        self.api_base = '/api/manufacturer/'

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
    pass
