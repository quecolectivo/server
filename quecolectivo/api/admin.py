from django.contrib.gis import admin
from .models import Line, Point, Polygon, Roads

@admin.register(Line, Point, Polygon, Roads)
class OSMAdmin(admin.OSMGeoAdmin):
    fields = ('way', 'osm_id', 'ref', 'name')