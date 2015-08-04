#import random
from random import gauss
from ann import *
def howMuchOfATautologyItIs(database, weights):
    out = 0.0
    n = len( database.datapoints[0].attributes)
    for i in range(100):
        lista = [0.0]*n
        for j in range(n):
            lista[j] = gauss(0,1)
        tmp = artificialNeuralNetwork(lista, weights)
        out += tmp*tmp
    return 1.0/(out+0.000001)
