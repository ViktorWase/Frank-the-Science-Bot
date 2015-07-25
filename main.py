"""
  This is the outline of a bot doing some science.
  It takes a dataset of objects with numerical values
  (like a database of planets with their size and RGB
  color and mass and stuff) and finds physical laws on
  the form f(objects) = 0. (conservations laws).
  Could probably derive some physics from a simple system.
"""

from ann import *
from dataObjectClass import *
from scienceFunctions import *

from simpleDatabase import *

def Frank(database, tol):
    exampleObj = database[0]
    #Generate a random function in the form of the parameters to an ANN which returns a single value.
    weightsOld = randomHypothesis(len(exampleObj.attributes))

    error = 100000000000000;
    errorOld = error
    while(error < tol):
        weights = addRandomLittleJump(list(weightsOld))
        error = 0
        #Iterate through all the elements in the database and see if the
        #ANN returns 0. Otherwise add the result to the error.
        for obj in database:
            error += someNorm(artificialNeuralNetwork(obj, weights))

        #Make sure it doesn't find conservation laws such as x-x=0.
        error += c1*howMuchOfATautologyItIs(weights)

        if(error<errorOld):
            errorOld = error
            weightsOld = list(weights)
            if(lawGoodEnough(database, weights)):
                func = translateFromANN2RegularMath(weights)
                return func


database = createSimpleDataSet( 3, 20 )

tol = 0.5

print Frank(database, tol)
