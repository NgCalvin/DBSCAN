from .models import Cluster

def clustering(radius, min_points, points):
    core_points = []
    for the_point in points:
        counter = 0
        for another_point in points:
            if the_point.distance(another_point) <= radius:
                counter += 1
            if counter >= min_points:
                core_points.append(the_point)
                break

    # TODO: return a list of Clusters
    return []
