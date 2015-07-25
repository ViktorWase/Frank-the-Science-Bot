import random

def someNorm(vector):
    """
        Lets go with the ordinary 2-norm.
    """
    tmpSum = 0.0
    for element in vector:
        tmpSum = tmpSum + element*element
    return sqrt(tmpSum)

def randomHypothesis(n):
    """
        Returns a set of weights in the form of
        a vector. These are to be used in the ANN.
        The idea is that this should return a random
        function. But a random ANN is the next best
        thing.
    """
    out = [0.0]*(220+10*n)
    for index in range(len(out)):
        if(random.random()<0.1):
            out[index] = 10.0*random.gauss(0.0,1.0)
    return out

def addRandomLittleJump(w):
    """
        Adds a small and random change to the
        weight vector.
    """
    for index in range(len(w)):
        #Try to keep the hypothesis sparse.
        if(w[index] != 0 or random.random() < 0.05):
            w[index] = w[index] + random.gauss(0.0, 0.05)
    return w
