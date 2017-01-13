from api.models import *
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.db.models import Q

p1 = Point(-57.976900, -34.894641, srid=4326)
p2 = Point(-57.955699, -34.910550, srid=4326)


def within(p, d):
    return Q(way__dwithin=(p, D(m=d)))


print(len(OsmLine.objects.filter(within(p1, 500) & within(p2, 500), route='bus')))
