from .models import Cluster

def getNeighbors(point, radius, min_points, points):
    neighbors = set()
    for another_point in points:
        if point.distance(another_point) <= radius:
            neighbors.add(another_point)
    return neighbors

def clustering(radius, min_points, points):

    # DBSCAN algorithm
    clusterId = 0
    for P in points:
        if P.clusterId is not None:
            continue
        neighbors = getNeighbors(P, radius, min_points, points)
        if len(neighbors) < min_points:
            P.assignCluster('Noise')
            continue
        clusterId += 1
        P.assignCluster(clusterId)
        connected_points = neighbors - set([P])
        while connected_points:
            Q = connected_points.pop()
            if Q.clusterId == 'Noise':
                Q.assignCluster(clusterId)
            if Q.clusterId is not None:
                continue
            Q.assignCluster(clusterId)
            neighbors = getNeighbors(Q, radius, min_points, points)
            if len(neighbors) >= min_points:
                connected_points |= neighbors

    # Group points into clusters
    clusters = []
    for P in points:
        if P.clusterId == 'Noise':
            continue
        cluster_exist = False
        for cluster in clusters:
            if P.clusterId == cluster.name:
                cluster.addPoint(P)
                cluster_exist = True
                break
        if cluster_exist:
            continue
        new_cluster = Cluster(name=P.clusterId)
        new_cluster.addPoint(P)
        clusters.append(new_cluster)
    
    return clusters
