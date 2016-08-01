import json
from django.http import JsonResponse
from indexer import es_api
from vehicles.models import VEHICLE_COLORS, VEHICLE_CATEGORY


# Create your views here.
def filters(request):
    aggs_service = es_api.get_aggreagation(
        'motor',
        'manufacturer.name',
        'category',
        'color',
        'engine',
    )
    aggs = aggs_service['aggregations']

    data = {
        'manufacturer': aggs['manufacturer.name']['buckets'],
        'motor': aggs['manufacturer.name']['buckets'],
        'category': aggs['category']['buckets'],
        'color': aggs['color']['buckets'],
        'engine': aggs['engine']['buckets'],
    }

    return JsonResponse(data)


def search(request):
    str_filters = request.GET.get('filters', '{}')
    filters = json.loads(str_filters)

    if 'manufacturer' in filters:
        filters['manufacturer.name'] = filters['manufacturer']
        del filters['manufacturer']

    data = es_api.search(
        request.GET.get('q'),
        **filters
    )
    return JsonResponse(data)
