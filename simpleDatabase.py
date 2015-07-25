from dataObjectClass import *
import random
def createSimpleDataSet( numOfAttr, numOfObj ):
    """
        This creates a simple data base with 3 attributes
        The second one is 2 times the first one with some
        Gauss noise. The third one is just random noise.
    """
    database = []
    for i in range(numOfObj):
        data = dataObject(numOfAttr)

        w=[random.gauss(2.0, 2.0)]
        w.append(w[0]*3+random.gauss(0.0, 0.05))
        w.append(random.random()*6)

        data.setAttributes([])
        database.append(data)
    return database
