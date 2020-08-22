#python manage.py ogrinspect home/data/Barangays/Barangays.shp TestData --srid=4326 --mapping --multi

import os
from django.contrib.gis.utils import LayerMapping
from .models import Barangay

# Auto-generated `LayerMapping` dictionary for Laguna model
laguna_mapping = {
    'City': 'NAME_2',
    'Name': 'NAME_3',
    'geom': 'MULTIPOLYGON',
}


laguna_mapping_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Laguna/Laguna.shp'))

def run(verbose=True):
    lm = LayerMapping(Barangay, laguna_mapping_shp, laguna_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



