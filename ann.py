from random import random
from math import fabs
from math import exp

from scienceFunctions import *

def sigmoidFunc(x):
        return x/(1.0+fabs(x))

def sigmoidFunc2(x):
        return 1.0/(1.0+exp(-x))-0.5

def isCorrectLength(obj,weights):
    try:
        n_o = len(obj)
        n_w = len(weights)

        if(n_o <= 0 or n_w <= 0):
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

def howManyWeightsInTheANN(hiddenLayers, numHiddenLayers, numInputs):
    """
        This calculates how many weights the ANN needs in order
        to function.
    """
    counter = (numInputs + 1)*hiddenLayers[0]
    for i in range(len(hiddenLayers)-1):
        counter += hiddenLayers[i]*hiddenLayers[i+1]
    counter += hiddenLayers[len(hiddenLayers)-1]
    return counter


def randomHypothesis(n, database):
    """
        Returns a set of weights in the form of
        a vector. These are to be used in the ANN.
        The idea is that this should return a random
        function. But a random ANN is the next best
        thing.

        It uses the Pearson r-correlation coefficient
        to find out which of the the attributes that
        might be connected.

        n is the number of inputs of the function.
    """
    #Generate the hidden layers!
    #The number of hidden layers is geometrically random
    numHiddenLayers = georand(0.8)
    hiddenLayers = [0]*numHiddenLayers
    #The number of nodes in each layer is geometrically random as well
    for i in range(numHiddenLayers):
        hiddenLayers[i] = georand(0.95)

    #How many weights are required in the ANN?
    numWeights = howManyWeightsInTheANN(hiddenLayers, numHiddenLayers, n)


    out = [0.0]*(numWeights+numHiddenLayers+1)
    out[0] = numHiddenLayers
    index = 1
    for element in hiddenLayers:
        out[index] = element
        index += 1

    #Decide which attributes that are important
    attributesInHypothesis = chooseAttributes(database, n)

    #Set the first row of the network
    numWeightsFirstRow = n*hiddenLayers[0]
    for i in range(hiddenLayers[0]):
        for j in range(n):
            if(attributesInHypothesis[j] == True):
                out[index] = random.gauss(0,10)
            index += 1

    #And then all of the other rows
    for i in range(numWeights-numWeightsFirstRow):
        if(random.random()<0.2):
            out[index] = 10.0*random.gauss(0.0,1.0)
        index += 1
    return out

def addRandomLittleJump(w):
    """
        Adds a small and random change to the
        weight vector.
    """
    out = list(w)

    counter = 1 + w[0]

    for index in range(len(w)-counter):
        #Try to keep the hypothesis sparse.
        if(w[index+counter] != 0 or random.random() < 0.05):
            out[index+counter] += random.gauss(0.0, 0.005)
    return out
