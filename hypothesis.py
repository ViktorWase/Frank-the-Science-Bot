import ann
import rbf
from tautology import *
from scienceFunctions import *

class Hypothesis:
    """
        This class contains a hypothesis.

        It should be able to be based on
        ANN, but in the future other things
        should be implemented as well.
    """
    def __init__(self, typeOfFunc, database, fitness = None, funcObj = None):
        self.type = typeOfFunc

        if(funcObj == None):
            if(self.type == "ANN"):
                #self.hypObj =
                raise NameError('Ann isnt fixed yet.')
                #self.randomHypothesis = ann.randomHypothesis
                #self.addRandomLittleJump = ann.addRandomLittleJump
                #self.function = ann.artificialNeuralNetwork
            elif(self.type == "RBF"):

                self.funcObj = rbf.radialBasisFunctionParameters(chooseAttributes(database, database.numAttributes), database)
                #self.randomHypothesis = rbf.randomHypothesis
                #self.addRandomJump = rbf.addRandomJump
                #self.function = rbf.radialBasisFunction
            elif(self.type == "NONE"):
                self.funcObj = None
            else:
                raise NameError('That is not a proper Hypothesis-type')
        else:
            self.funcObj = funcObj

        if fitness == None:
            self.fitness = -1000000000000000000000000000
        else:
            self.fitness = fitness

    def getRandom(self, database):
        self.funcObj.randomHypothesis(database)

    def getFitness(self):
        return self.fitness

    def function( self, x ):
        if(self.type == "RBF"):
            return self.funcObj.radialBasisFunction(x)
        else:
            raise NameError('That is not a proper function type.')

    def checkNeighbour(self, database):
        tmpFuncObj = self.funcObj.getNeig_copy(database)
        tmpHyp = Hypothesis("NONE", None)
        tmpHyp.funcObj = tmpFuncObj
        tmpHyp.type = self.type

        tmpHyp.updateAndReturnFitness(database, 1.0)
        self.updateAndReturnFitness(database, 1.0)
        if tmpHyp.getFitness() > self.getFitness() :
            self.fitness = tmpHyp.getFitness()
            self.funcObj = tmpHyp.funcObj

    def updateAndReturnFitness(self, database, c1):
        error = 0
        for obj in database.datapoints:
            tmp = self.function(obj.attributes)
            error += tmp*tmp
        #Make sure it doesn't find conservation laws such as x-x=0.
        tmp = howMuchOfATautologyItIs(database, self)
        error += c1*tmp*tmp
        self.fitness = -error
        return self.fitness

    def calcAndReturnFitness(self, database, c1):
        error = 0
        for obj in database.datapoints:
            tmp = self.function(obj.attributes)
            error += tmp*tmp
        #Make sure it doesn't find conservation laws such as x-x=0.
        tmp = howMuchOfATautologyItIs(database, self)
        error += c1*tmp*tmp
        #self.fitness = -error
        return -error

    def returnCopy(self):
        funcObjCopy =  self.funcObj.returnCopy()
        return Hypothesis( self.type, None, self.getFitness, funcObjCopy)
