'''
Created on 5 Dec 2017

@author: ngwinghin
'''
import os
import sys

from pointSorting import pointSorting

if __name__ == '__main__':
    if len(sys.argv) != 3:
        try:
            script_name = sys.argv[0]
        except IndexError:
            script_name = 'CorePoint.py'
        print('Usage: python {} <Radius> <Support>'.format(script_name))
        exit(1)
        
    radius = sys.argv[1]
    support = sys.argv[2]
    
    ps = pointSorting()
    corePoint = ps.getCorePoint(radius,support)
    print corePoint
    print len(corePoint)