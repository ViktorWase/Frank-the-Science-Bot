from random import random
from math import fabs
from math import exp

import scienceFunctions

def sigmoidFunc2(x):
        return x/(1.0+fabs(x))

def sigmoidFunc(x):
        return 1.0/(1.0+exp(-x))-0.5

def isCorrectLength(obj,weights):
    try:
        n_o = len(obj)
        n_w = len(weights)

        if(n_o<=0 or n_w <= 0):
            return False

        hiddenLayers = weights[1:(weights[0]+1)]
        if(len(hiddenLayers) != weights[0]):
            print "fuck"

        counter = len(hiddenLayers) + 1
        counter += (n_o + 1)*hiddenLayers[0]
        for i in range(len(hiddenLayers)-1):
            counter += hiddenLayers[i]*hiddenLayers[i+1]
        counter += hiddenLayers[len(hiddenLayers)-1]

        if(n_w != counter):
            return False

    except:
        return False

    return True


def artificialNeuralNetwork(obj, weights):
    """
        obj is a list of values (like [0.5, 6.0, 0]. Keep away
        from inf and nan and stuff).

        weights is a vector where the first element is the number
        of hidden layers. (Call it N)
        Then there should follow N integers that show how many nodes
        there should be in the N hidden layers.
        Then there are a fuckbunch of floats that symbolize the actual
        parameters (or weights) of the neural network.
    """
    oldLayer = list(obj)

    #Prepares the stuff for the network.
    hiddenLayers = weights[0]
    counter = 1
    nodesInHiddenLayers = []
    for i in range(hiddenLayers):
        nodesInHiddenLayers.append(weights[counter])
        counter += 1

    #Always add a one to avoid bias
    oldLayer.append(1.0)

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
    #print counter

    return out
