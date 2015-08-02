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
from tautology import *

from simpleDatabase import *

def lawGoodEnough(w, data, c2):
    """
        This takes 30% of the database
        and checks if the hypothesis still
        holds, even though the hypothesis
        was developed using the other 70%
        of the data.

        Uses a sort of l2-norm. Kind of.

        c2 needs some serious tuning.
    """
    error = 0
    for obj in data.datapoints:
        error += artificialNeuralNetwork(obj.attributes, w)**2
    error = error /data.numElements
    if error < c2:
        return True
    else:
        return False

def Frank(database, verificationDatabase, tol, c1, c2):
    exampleObj = database.datapoints[0]
    #Generate a random function in the form of the parameters to an ANN which returns a single value.
    weightsOld = randomHypothesis(len(exampleObj.attributes), database)

    error = 100000000000000
    errorOld = error
    while(errorOld > tol):
        weights = addRandomLittleJump(list(weightsOld))
        error = 0
        #Iterate through all the elements in the database and see if the
        #ANN returns 0. Otherwise add the result to the error.
        for obj in database.datapoints:
            tmp = (artificialNeuralNetwork(obj.attributes, weights))
            error += tmp*tmp
        #Make sure it doesn't find conservation laws such as x-x=0.
        error += c1*howMuchOfATautologyItIs(database, weights)

        if(error<errorOld):
            errorOld = error
            print error
            weightsOld = list(weights)
            if(lawGoodEnough(weights, verificationDatabase, c2)):
                #print weights
                func = translateFromANN2RegularMath(weights)
                return func

#Create a simple database with 3 attributes
#to each of the 20 objects
database = createSimpleDataSet( 3, 20 )

#Shuffle the database to make sure that
#everything is nice and random.
random.shuffle(database)

n=len(database)
#Use 70% of the database to create the hypothesis
numberOfTestElements = int(n*0.7)
#Use the rest to make sure that it's a good hypothesis
numberOfVerificationElements = n- numberOfTestElements

verificationDatabase = Database(database[0:numberOfVerificationElements])
database = Database(database[numberOfVerificationElements:n])

#These are NOT correct in any way. Tune them!
tol = 0.5
c1 = 1.0
c2 = 0.7

print Frank(database, verificationDatabase, tol, c1, c2)
