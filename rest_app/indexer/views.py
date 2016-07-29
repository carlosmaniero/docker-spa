from django.http import JsonResponse
from indexer import es_api
from vehicles.models import VEHICLE_COLORS, VEHICLE_CATEGORY


# Create your views here.
def filters(self):
    aggs_service = es_api.get_aggreagation(
        'motor',
        'manufacturer.name',
        'category',
        'color'
    )
    aggs = aggs_service['aggregations']

    data = {
        'manufacturer': aggs['manufacturer.name']['buckets'],
        'motor': aggs['manufacturer.name']['buckets'],
        'category': aggs['category']['buckets'],
        'color': aggs['color']['buckets']
    }

    return JsonResponse(data)
