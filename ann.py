from random import random
from math import fabs

def sigmoidFunc(x):
        return x/(1.0+fabs(x))

def artificialNeuralNetwork(obj, weights):
    """
        obj is a list of values (like [0.5, 6.0, 0]. Keep away
        from inf and nan and stuff).
        weights is a list of values as well. It should be of size
        220+10*len(obj). Dunno why.
    """
    oldLayer = list(obj.attributes)

    #These are ad hoc as fuck and should probably be fixed.
    hiddenLayers = 3
    nodesInHiddenLayers = [10, 10, 10]

    #Always add a one to avoid bias
    oldLayer.append(1.0)

    #Sometimes add a random to instil fear in the hearts of your enemies
    #But not today.
    isRandom = False
    if(isRandom):
        oldLayer.append(2.0*random()-1.0)

    counter = 0
    for i in range(hiddenLayers):
        layer = [0.0]*nodesInHiddenLayers[i]
        for j in range(len(layer)):
            for k in range(len(oldLayer)):
                layer[j] += oldLayer[k]*weights[counter]
                counter += 1
            layer[j] = sigmoidFunc(layer[j])
        oldLayer = list(layer)

    #Final layer
    out = 0.0
    for i in range(nodesInHiddenLayers[hiddenLayers-1]):
        out += layer[i]*weights[counter]
        counter += 1
    print counter

    return out
