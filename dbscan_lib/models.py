import math

from collections import namedtuple

_point_model = namedtuple('Point', ['x', 'y'])

class Point(_point_model):
    def __init__(self, x, y):
        self._clusterId = None

    @property
    def clusterId(self):
        return self._clusterId

    def assignCluster(self, clusterId):
        self._clusterId = clusterId

    def __str__(self):
        return 'Point(Cluster: {}, [{},{}])'.format(self.clusterId, self.x, self.y)

    def distance(self, another_point):
        return math.sqrt(
            (self.x - another_point.x) ** 2 +
            (self.y - another_point.y) ** 2
        )

class Cluster:
    def __init__(self, name=None, points=None):
        self._name = name
        self._points = set() if points is None else points

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return list(self._points)

    def __str__(self):
        return 'Cluster(name="{}")'.format(self.name)

    def getSize(self):
        return len(self._points)

    def addPoint(self, point):
        self._points.add(point)

    def hasPoint(self, point):
        return (point in self._points)
