from scienceFunctions import georand
from random import randint
from random import random

def linCombRand(database):
    """
        Takes a random number of points from
        the database and returns a vector that
        is a randomly weighted linear combination
        of the points.
    """
    numPoints = georand(0.8)
    out = [0.0]*database.numAttributes
    for i in range(numPoints):
        rand1 = randint(0,database.numElements-1)
        rand2 = randint(0,database.numElements-1)
        w = random()
        for j in range(database.numAttributes):
            out[j] = out[j] + database.datapoints[rand1].attributes[j]*w + database.datapoints[rand1].attributes[j] * (1-w)
    for i in range(database.numAttributes):
        out[i] = out[i]/numPoints
    return out
