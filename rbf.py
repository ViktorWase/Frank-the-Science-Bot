"""
    This is a way of representing random functions.
    It could propably by used instead of ANN. I'm
    not sure which is best actually.
"""
from tautology import *
import random
from scienceFunctions import *

class radialBasisFunctionParameters:
    def __init__(self, chosenAttributes, database = None, numFunctions = None, w_list = None, xc_list = None):
        self.chosenAttributes = chosenAttributes
        self.dim = 0
        self.numFunctions = None
        self.w = None
        self.xc = None
        for attr in chosenAttributes:
            if attr == True:
                self.dim += 1
            elif attr == False:
                pass
            else:
                raise NameError("That's not a bool!")

        if(numFunctions == None and w_list == None and xc_list == None ):
            self.numFunctions = georand(0.992)
            if( database == None ):
                raise NameError("NO! Send a database as well.")
            else:
                self.randomHypothesis(database)

        elif(numFunctions == None or w_list == None or xc_list == None ):
            raise NameError("Pass all 4 arguments to radialBasisFunctionParameter")
        else:
            self.numFunctions = numFunctions
            self.w = w_list
            self.xc = xc_list

    def randomHypothesis( self, database):
        if (self.xc == None):
            self.xc = [0.0] * self.numFunctions * self.dim
        for i in range(self.numFunctions * self.dim):
            self.xc[i] = random.gauss(0,10)

        if(self.w == None):
            self.w = [0.0] * self.numFunctions
        for i in range(self.numFunctions):
            self.w[i] += random.gauss(0, 5000)

    def addRandomJump(self):
        for i in range(self.numFunctions * self.dim):
            self.xc[i] += random.gauss(0,0.5)

        for i in range(self.numFunctions):
            self.w[i] += random.gauss(0, 0.5)

    def getNeig_copy( self, database ):
        xc_copy = list(self.xc)
        w_copy = list(self.w)

        hyp_copy = radialBasisFunctionParameters(self.chosenAttributes, database, self.numFunctions, w_copy, xc_copy)
        hyp_copy.addRandomJump()
        return hyp_copy

    def returnCopy(self):
        xc_copy = list(self.xc)
        w_copy = list(self.w)
        chosenAttributes_copy = list(self.chosenAttributes)

        hyp_copy = radialBasisFunctionParameters(chosenAttributes_copy, None, self.numFunctions, w_copy, xc_copy)
        return hyp_copy

    def wavelet(self, p_2, xc, x):
        r = 0
        for i in range(len(xc)):
            r = (xc[i]-x[i]) * (xc[i]-x[i])
        return 1.0/(1.0+p_2*r)

    def radialBasisFunction(self, x):
        out = 0
        for i in range( self.numFunctions ):
            out += self.wavelet( self.w[i], self.xc[i*self.dim : (i+1)*self.dim], x )
        return out

    """def soHowGoodIsItAnyway(self, database):
        for obj in database.datapoints:
            tmp = self.radialBasisFunction(obj.attributes)
            error += tmp*tmp
        #Make sure it doesn't find conservation laws such as x-x=0.
        tmp = howMuchOfATautologyItIs(database, weights)
        error += c1*tmp*tmp
        return error"""
