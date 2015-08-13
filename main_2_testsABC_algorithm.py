from artificialBeeColony import *
#from ann import *
from rbf import *
from dataObjectClass import *
from scienceFunctions import *
from hypothesis import *
from simpleDatabase import *
from main import *

def getHypObj(database):
    chosen = chooseAttributes(database, database.numAttributes)
    if (random.random() < 1.5):
        hyp = Hypothesis( "RBF" , database )
    else:
        hyp = Hypothesis( "ANN" , database )
    return hyp

def FrankABC(database, verificationDatabase):

    colony = Colony(database, 30,30, getHypObj)
    bestHyp = colony.findBestFlower(100)
    #print "x: ",

    print "Klar!"

    print bestHyp.function([0,0,0])
    print bestHyp.function([1,0,0])
    print bestHyp.function([0,1,0])
    print bestHyp.function([0,0,1])
    print bestHyp.function([1,2,0])
    print bestHyp.function([1,2,1])
    print bestHyp.function([1,2,2])



    """
    print artificialNeuralNetwork([0,0,0], weights)
    print artificialNeuralNetwork([1,0,0], weights)
    print artificialNeuralNetwork([0,1,0], weights)
    print artificialNeuralNetwork([0,0,1], weights)
    print artificialNeuralNetwork([1,2,0], weights)
    print artificialNeuralNetwork([1,2,1], weights)
    print artificialNeuralNetwork([1,2,2], weights)
    #print fit(bestSolution)
    """




#Create a simple database with 3 attributes
#to each of the 20 objects
database = createSimpleDataSet( 3, 100 )

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
tol = 0.05
c1 = 5.0
c2 = 0.001

FrankABC(database, verificationDatabase)
