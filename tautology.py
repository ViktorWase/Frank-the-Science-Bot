#import random
from random import gauss
#from ann import *
def howMuchOfATautologyItIs(database,hyp):
    out = 0.0
    n = database.numAttributes
    for i in range(500):
        lista = [0.0]*n
        for j in range(n):
            lista[j] = gauss(0,10.0)
        tmp = hyp.function(lista)
        out += tmp*tmp
    return 1.0/(out+0.000001)
