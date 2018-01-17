from injector import Binder
from services.elasticsearch import ElasticSearchIndex, ElasticSearchFactory
from es_mapping import room_mapping
import os


def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticSearchIndex,
        ElasticSearchIndex(
            ElasticSearchFactory(
                os.environ['ELASTICSEARCH_HOST'],
                os.environ['ELASTICSEARCH_PORT'],
            ),
            'rooms',
            'room',
            room_mapping
        )
    )
    return binder
