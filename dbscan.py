import argparse
import os.path
import sys


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
