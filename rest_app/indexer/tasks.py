from celery.utils.log import get_task_logger
from rest_app import celery_app
from vehicles.models import Vehicle
from vehicles.serializers import EsVehicleSerializer
from indexer.es_api import index_vehicle, ESIndexException

logger = get_task_logger(__name__)


@celery_app.task(name='index_vehicles')
def index_vehicles():
    vehicles = Vehicle.objects.select_related(
        'manufacturer'
    ).all().order_by('-indexed_at')

    for vehicle in vehicles:
        vehicle_data = EsVehicleSerializer(vehicle).data
        logger.info('Indexando o carro {}'.format(
            vehicle_data['model_name']
        ))
        try:
            index_vehicle(vehicle_data)
        except ESIndexException as e:
            logger.error(e.data)
            continue
        vehicle.update_index_time()
