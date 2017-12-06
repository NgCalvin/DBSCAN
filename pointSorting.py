'''
Created on 5 Dec 2017

@author: ngwinghin
'''

class pointSorting(object):
    '''
    classdocs
    '''
    def get_point(cls):
        return [[31.95,7.95],[31.15,7.3],[30.45,6.65],[29.7,6],[28.9,5.55],[28.05,5],[27.2,4.55],[26.35,4.15],
[25.4,3.85],[24.6,3.6],[23.6,3.3],[22.75,3.15],[21.85,3.05],[20.9,3],[20,2.9],[19.1,3],
[18.2,3.2],[17.3,3.25],[16.55,3.5],[15.7,3.7],[14.85,4.1],[14.15,4.4],[13.4,4.75],[12.7,5.2],
[12.05,5.65],[11.45,6.15],[10.9,6.65],[10.3,7.25],[9.7,7.85],[9.35,8.35],[8.9,9.05],[8.55,9.65],
[8.15,10.35],[7.95,10.95],[7.75,11.7],[7.55,12.35],[7.45,13],[7.35,13.75],[7.3,14.35],[7.35,14.95],
[7.35,15.75],[7.55,16.35],[7.7,16.95],[7.8,17.55],[8.05,18.15],[8.3,18.75],[8.65,19.3],[8.9,19.85],
[9.3,20.3],[9.65,20.8],[10.2,21.25],[10.6,21.65],[11.1,22.15],[11.55,22.45],[11.95,22.7],[12.55,23],
[13.05,23.2],[13.45,23.4],[14,23.55],[14.55,23.6],[15.1,23.75],[15.7,23.75],[16.15,23.85],[16.7,23.8],
[17.15,23.75],[17.75,23.75],[18.2,23.6],[18.65,23.5],[19.1,23.35],[19.6,23.15],[20,22.95],[20.4,22.7],
[20.7,22.55],[21,22.15],[21.45,21.95],[21.75,21.55],[22,21.25],[22.25,21],[22.5,20.7],[22.65,20.35],
[22.75,20.05],[22.9,19.65],[23,19.35],[23.1,19],[23.15,18.65],[23.2,18.25],[23.2,18.05],[23.2,17.8],
[23.1,17.45],[23.05,17.15],[22.9,16.9],[22.85,16.6],[22.7,16.4],[22.6,16.2],[22.55,16.05],[22.4,15.95],
[22.35,15.8],[22.2,15.65],[22.15,15.55],[22,15.4],[21.9,15.3],[21.85,15.25],[21.75,15.15],[21.65,15.05],
[21.55,15],[21.5,14.9],[19.35,31.65],[20.35,31.45],[21.35,31.1],[22.25,30.9],[23.2,30.45],[23.95,30.05],
[24.9,29.65],[25.6,29.05],[26.35,28.5],[27.15,27.9],[27.75,27.35],[28.3,26.6],[28.95,25.85],[29.5,25.15],
[29.95,24.45],[30.4,23.7],[30.6,22.9],[30.9,22.1],[31.25,21.3],[31.35,20.55],[31.5,19.7],[31.55,18.9],
[31.65,18.15],[31.6,17.35],[31.45,16.55],[31.3,15.8],[31.15,15.05],[30.9,14.35],[30.6,13.65],[30.3,13],
[29.9,12.3],[29.5,11.75],[29,11.15],[28.5,10.6],[28,10.1],[27.55,9.65],[26.9,9.1],[26.25,8.8],
[25.7,8.4],[25.15,8.05],[24.5,7.75],[23.9,7.65],[23.15,7.4],[22.5,7.3],[21.9,7.1],[21.25,7.05],
[20.5,7],[19.9,6.95],[19.25,7.05],[18.75,7.1],[18.05,7.25],[17.5,7.35],[16.9,7.6],[16.35,7.8],
[15.8,8.05],[15.4,8.35],[14.9,8.7],[14.45,8.9],[13.95,9.3],[13.6,9.65],[13.25,10.1],[12.95,10.55],
[12.65,10.9],[12.35,11.4],[12.2,11.75],[11.95,12.2],[11.8,12.65],[11.75,13.05],[11.55,13.6],[11.55,14],
[11.55,14.35],[11.55,14.7],[11.6,15.25],[11.65,15.7],[11.8,16.05],[11.85,16.5],[12,16.75],[12.15,17.2],
[12.3,17.6],[12.55,17.85],[12.8,18.05],[13.1,18.4],[13.3,18.6],[13.55,18.85],[13.8,19.05],[14.15,19.25],
[14.45,19.5],[14.85,19.55],[15,19.7],[15.25,19.7],[15.55,19.85],[15.95,19.9],[16.2,19.9],[16.55,19.9],
[16.85,19.9],[17.2,19.9],[17.4,19.8],[17.65,19.75],[17.8,19.7],[18,19.6],[18.2,19.55],[3.9,9.6],
[3.55,10.65],[3.35,11.4],[3.1,12.35],[3.1,13.25],[3.05,14.15],[3,15.1],[3.1,16],[3.2,16.85],
[3.45,17.75],[3.7,18.7],[3.95,19.55],[4.35,20.25],[4.7,21.1],[5.15,21.8],[5.6,22.5],[6.2,23.3],
[6.8,23.85],[7.35,24.45],[8.05,24.95],[8.8,25.45],[9.5,26],[10.2,26.35],[10.9,26.75],[11.7,27],
[12.45,27.25],[13.3,27.6],[14.05,27.6],[14.7,27.75],[15.55,27.75],[16.4,27.75],[17.1,27.75],[17.9,27.75],
[18.55,27.7],[19.35,27.6],[20.1,27.35],[20.7,27.1],[21.45,26.8],[22.05,26.5],[22.7,26.15],[23.35,25.65],
[23.8,25.3],[24.3,24.85],[24.75,24.35],[25.25,23.95],[25.65,23.45],[26.05,23],[26.2,22.3],[26.6,21.8],
[26.75,21.25],[27,20.7],[27.15,20.15],[27.15,19.6],[27.35,19.1],[27.35,18.45],[27.4,18],[27.3,17.4],
[27.15,16.9],[27,16.4],[27,15.9],[26.75,15.35],[26.55,14.85],[26.3,14.45],[25.95,14.1],[25.75,13.7],
[25.35,13.3],[25.05,12.95],[24.8,12.7],[24.4,12.45],[24.05,12.2],[23.55,11.85],[23.2,11.65],[22.75,11.4],
[22.3,11.3],[21.9,11.1],[21.45,11.05],[21.1,11],[20.7,10.95],[20.35,10.95],[19.95,11],[19.55,11],
[19.15,11.05],[18.85,11.1],[18.45,11.25],[18.15,11.35],[17.85,11.5],[17.5,11.7],[17.2,11.95],[17,12.05],
[16.75,12.2],[16.65,12.35],[16.5,12.5],[16.35,12.7],[16.2,12.8],[16.15,12.95],[16,13.1],[15.95,13.25],
[15.9,13.4],[15.8,13.5],[15.8,13.65],[15.75,13.85],[15.65,14.05],[15.65,14.25],[15.65,14.5],[15.65,14.6]]

    def getCorePoint(self,radius,support):
        '''
        Constructor
        '''
        pointList = self.get_point()
        print len(pointList)
        sortedList = sorted(pointList,key=lambda x: (x[0],x[1]))
        corePoint = []
        
        for row in sortedList:
            counter = 0
            for checker in sortedList:
                if  float(radius)**2 >= (float(checker[0])-float(row[0]))**2 + (float(checker[1])-float(row[1]))**2:
                    counter = counter + 1
                    if int(counter) >= int(support):
                        corePoint.append(row)
                        break
        return corePoint
        
        
        
        
    