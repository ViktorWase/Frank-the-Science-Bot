"""
Finds an approximate function to an artificial neural network.
"""
from simpleDatabase import *
from hypothesis import Hypothesis

from pygep.functions.mathematical.arithmetic import (add_op, subtract_op, multiply_op, divide_op)
from pygep.functions.linkers import sum_linker
from pygep import *
import random

class DataPoint():
    DATA_POINTS = []
    SAMPLE_SIZE = 10

    def __init__(self, hypo, x):
        self.x = float(x)
        self.y = hypo.function(self.x); # this is the function we want to find

    @staticmethod
    def populate(hypo, low = -100, high = 100):
        range_size = high - low
        # Creates random data points
        DataPoint.DATA_POINTS = []
        for _ in xrange(DataPoint.SAMPLE_SIZE):
            x = low + (random.random() * range_size)
            DataPoint.DATA_POINTS.append(DataPoint(hypo, x))

class Regression(Chromosome):
    REWARD = 1000.0
    functions = multiply_op, add_op, subtract_op, divide_op
    terminals = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'x'
    
    def _fitness(self):
        total = 0
        for x in DataPoint.DATA_POINTS:
            try:
                guess = self(x) # Evaluation of this chromosome
                diff = min(1.0, abs((x.y - guess) / x.y))
                total += self.REWARD * (1 - diff)
                                
            except ZeroDivisionError: # semantic error
                pass

        return total
    
    def _solved(self):
        return self.fitness == self.max_fitness

    max_fitness = property(lambda self: self.REWARD * DataPoint.SAMPLE_SIZE)


class ANNMath:

    def __init__(self, hypo):
        self.hypo = hypo
        pass

    def approx(self, llimit = -100, hlimit = 100):
        DataPoint.populate(self.hypo, llimit, hlimit) # create some new data points

        # Search for a solution
        p = Population(Regression, 10, 2, 2, sum_linker)
        print p

        for _ in xrange(100):
            if p.best.solved:
                break
            p.cycle()
            print
            print p
            
        print
        print 'Best: ', p.best

        if p.best.solved:
            print 'SOLVED!'

if __name__ == '__main__':
    #TODO: Change variable names >.>
    #Create a simple database with 3 attributes to each of the 20 objects
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

    hypo = Hypothesis('RBF', database)

    annm = ANNMath(hypo)
    # find approximation
    annm.approx()
