import django_tables2 as tables
from .models import Incident
import itertools


class IncidentTable(tables.Table):
    def __init__(self, fieldList):
        class Meta:
            fields = (fieldList,)

