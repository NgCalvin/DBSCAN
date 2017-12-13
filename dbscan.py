import argparse
import os.path
import sys

from dbscan_lib import Point, clustering


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Basic DBSCAN Implementation')
    arg_parser.add_argument('radius',
                            metavar='RADIUS',
                            type=float,
                            help='radius of the vicinity area of each point')
    arg_parser.add_argument('min_points',
                            metavar='MIN_POINTS',
                            type=int,
                            help='minimum points in vicinity area of'
                                 'main points')
    arg_parser.add_argument('data_file',
                            metavar='DATA_FILE',
                            help='data file to be read')
    args = arg_parser.parse_args()

    if os.path.exists(args.data_file) is not True:
        print('File "{}" does not exist'.format(args.data_file),
              file=sys.stderr)
        exit(1)

    make_clusters = lambda pts: clustering(args.radius,
                                           args.min_points,
                                           pts)
    with open(args.data_file) as data_file:
        points = set()

        line = data_file.readline()
        while(len(line) > 0):
            point_x, point_y = line.rstrip('\n').split('\t', maxsplit=1)
            new_point = Point(x=float(point_x), y=float(point_y))
            points.add(new_point)
            line = data_file.readline()

        clusters = make_clusters(points)
        if len(clusters) == 0:
            print('No clusters are found', file=sys.stderr)
            exit(0)

        for cluster_idx, each_cluster in enumerate(clusters):
            for each_point in each_cluster.points:
                print('{}\t{}\t{}'.format(each_point.x,
                                          each_point.y,
                                          cluster_idx))
