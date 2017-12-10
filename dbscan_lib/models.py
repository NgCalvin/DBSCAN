import math

from collections import namedtuple

_point_model = namedtuple('Point', ['x', 'y'])

class Point(_point_model):
    def distance(self, another_point):
        return math.sqrt(
            (self.x - another_point.x) ** 2 +
            (self.y - another_point.y) ** 2
        )

class Cluster:
    def __init__(self, name='', points=set()):
        self._name = name
        self._points = points

    @property
    def name(self):
        return list(self._name)

    @property
    def points(self):
        return list(self._points)

    def __str__(self):
        return 'Cluster(name="{}")'.format(self.name)

    def addPoint(self, point):
        self._points.add(point)

    def hasPoint(self, point):
        return (point in self._points)
