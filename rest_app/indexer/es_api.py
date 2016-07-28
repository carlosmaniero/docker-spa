import json
import requests
from django.conf import settings

VEHICLE_BASE_URL = '{}/vehicles/'.format(
    settings.ELASTICSEARCH_HOST
)
VEHICLE_URL = '{}/vehicles/vehicle/'.format(
    settings.ELASTICSEARCH_HOST
)


class ESIndexException(BaseException):
    ''' Raised if can't index the data in Elasticsearch '''
    def __init__(self, data):
        try:
            self.data = json.loads(data.decode())
        except ValueError:
            self.data = {
                'error': data
            }


def get_vehicle_url(vehicle_id):
    ''' Get vehicle es-url '''
    return '{}{}'.format(VEHICLE_URL, vehicle_id)


def get_vehicle(vehicle_id):
    ''' Get a vehicle from Elasticsearch '''
    try:
        response = requests.get(
            get_vehicle_url(vehicle_id),
        )
    except Exception as e:
        return ESIndexException(bytes(e))

    if response.status_code not in (200, 201):
        raise ESIndexException(response.content)

    return json.loads(response.content.decode())


def index_vehicle(vehicle_data):
    ''' Add a vehicle to the elasticsearch '''
    try:
        response = requests.post(
            get_vehicle_url(vehicle_data['id']),
            data=json.dumps(vehicle_data)
        )
    except Exception as e:
        return ESIndexException(bytes(e))

    if response.status_code not in (200, 201):
        raise ESIndexException(response.content)

    return json.loads(response.content.decode())


def get_aggreagation(*keys):
    ''' Return keys aggregations '''
    query = {
        "size": 0,
        "aggregations": {
        }
    }

    for key in keys:
        query['aggregations'][key] = {
            "terms": {
                "field": key
             }
        }

    try:
        response = requests.post(
            VEHICLE_URL + '_search',
            data=json.dumps(query)
        )
    except Exception as e:
        return ESIndexException(bytes(e))

    if response.status_code not in (200, 201):
        raise ESIndexException(response.content)

    return json.loads(response.content.decode())
