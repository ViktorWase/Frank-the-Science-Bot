import random

from r_coefficient import *

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

def georand(p):
    """
        This is the geometric distribution with
        parameter p. They didn't have it in the
        Random library. Not sure why.
    """
    if(p<0 or p>1.0):
        print "p should be between 0 and 1 (georand)"
        return

    counter = 1
    while(random.random() <= p):
        counter += 1
    return counter

def someNorm(vector):
    """
        Lets go with the ordinary 2-norm.
    """
    tmpSum = 0.0
    for element in vector:
        tmpSum = tmpSum + element*element
    return sqrt(tmpSum)

def chooseAttributes(database, n):
    """
        Choose which elements that should be used in the hypothesis.
        This is based on their Pearson r coefficient.
    """
    attributes = [False]*n
    for index in range(n*n):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        if x != y:
            X = database.getVectorWithAttributeNr(x)
            Y = database.getVectorWithAttributeNr(y)
            if(abs(pearson_r_correlation( X ,Y )) > random.random()):
                if(attributes[x] == False):
                    attributes[x] = True
                if(attributes[y] == False):
                    attributes[y] = True

    #And we add 2 random attributes, just to spice it up
    attributes[random.randint(0,n-1)] = True
    attributes[random.randint(0,n-1)] = True
    return attributes

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
