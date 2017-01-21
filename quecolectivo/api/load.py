import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

osmpoint_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data',
                 'TM_WORLD_BORDERS-0.3.shp'),
)


def run(verbose: bool =True):
    lm = LayerMapping(
        WorldBorder, world_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

