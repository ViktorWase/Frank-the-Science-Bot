"""
    This is a way of representing random functions.
    It could propably by used instead of ANN. I'm
    not sure which is best actually.
"""
from tautology import *
import random


class radialBasisFunctionParameters:
    def __init__(self, chosenAttributes, numFunctions, w_list, xc_list ):
        self.numFunctions = numFunctions
        self.w = w_list
        self.xc = xc_list
        self.chosenAttributes = chosenAttributes
        self.dim = 0
        for attr in chosenAttributes:
            if attr == True:
                self.dim += 1
            elif attr == False:
                pass
            else:
                raise NameError("That's not a bool!")

    def randomHypothesis(n, database):
        for i in range(self.numFunctions * dim):
            self.xc[i] = random.gauss(0,5000)

        for i in range(self.numFunctions):
            self.w[i] += random.gauss(0, 50)

    def addRandomJump(parameters):
        for i in range(self.numFunctions * self.dim):
            self.xc[i] += random.gauss(0,0.005)

        for i in range(self.numFunctions):
            self.w[i] += random.gauss(0, 0.005)


    def wavelet(p_2, xc, x):
        r = 0
        for i in range(len(xc)):
            r = (xc[i]-x[i]) * (xc[i]-x[i])
        return 1.0/(1.0+p_2*r)

    def radialBasisFunction(x,parameters):
        out = 0
        for i in range( self.numFunctions ):
            out += self.wavelet( parameters.w[i], parameters.xc[i*self.dim : (i+1)*self.dim], x )
        return out

    def soHowGoodIsItAnyway(database, hyp):
        for obj in database.datapoints:
            tmp = radialBasisFunction(obj.attributes, hyp)
            error += tmp*tmp
        #Make sure it doesn't find conservation laws such as x-x=0.
        tmp = howMuchOfATautologyItIs(database, weights)
        error += c1*tmp*tmp
