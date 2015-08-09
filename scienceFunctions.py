import random

from r_coefficient import *

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
    attributes = [False for i in range(n)]
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
