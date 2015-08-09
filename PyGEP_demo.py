from pygep.functions.mathematical.arithmetic import (add_op, subtract_op, multiply_op, divide_op)
from pygep.functions.linkers import sum_linker
from pygep import *
import random

class Data():
    DATA_POINTS = []
    SAMPLE_SIZE = 10
    RANGE_LOW, RANGE_HIGH = -100, 100
    RANGE_SIZE = RANGE_HIGH - RANGE_LOW

    def __init__(self, x):
        self.x = float(x)
        self.y = x+x*x; # this is the function we want to find

    @staticmethod
    def populate():
        # Creates random data points
        Data.DATA_POINTS = []
        for _ in xrange(Data.SAMPLE_SIZE):
            x = Data.RANGE_LOW + (random.random() * Data.RANGE_SIZE)
            Data.DATA_POINTS.append(Data(x))

class Regression(Chromosome):
    REWARD = 1000.0
    functions = multiply_op, add_op, subtract_op, divide_op
    terminals = 1, 2, 'x',
    
    def _fitness(self):
        total = 0
        for x in Data.DATA_POINTS:
            try:
                guess = self(x) # Evaluation of this chromosome
                diff = min(1.0, abs((x.y - guess) / x.y))
                total += self.REWARD * (1 - diff)
                                
            except ZeroDivisionError: # semantic error
                pass

        return total
    
    def _solved(self):
        return self.fitness == self.max_fitness

    max_fitness = property(lambda self: self.REWARD * Data.SAMPLE_SIZE)

# Converts an equation in karva notation to standard notation.
# TODO: Find out how the notation ACUTALLY works.
def karvaToStandard(p):
    s = str(p)
    binop = ['+','-','/','*']

    T = []
    i = 0
    t = 0
    for i, c in enumerate(s):
        if t < len(T):
            t = len(T)
        if c in binop:
            T.append((c, t+1, t+2))
            t += 2
        else:
            T.append((c,))
            t += 0
        #print i, T[i]

    def iterator(i):
        if len(T[i]) == 3:
            l = iterator(T[i][1])
            r = iterator(T[i][2])
            depth = max(l[0], r[0])
            return depth, '(' + l[1] + T[i][0] + r[1] + ')'
        return i, T[i][0]

    result = ''
    const = False
    depth = 0
    while depth < len(T):
        d, s = iterator(depth)
        c = len(s) == 1
        if not c or depth == 0: # not const or not c:
            if depth > 0:
                result += '+'
            result += s
        const = c
        depth = d + 1
        #print depth, s

    return result

if __name__ == '__main__':
    # The following examples should be x+x*x (but are not)
    #print karvaToStandard('x+2x2**1xx')
    #print karvaToStandard('x+x11**xx1')
    #print karvaToStandard('xx222/*1xx')
    #print karvaToStandard('x-212*xx1x')
    #print karvaToStandard('2-2x1/*xx2')
    #print karvaToStandard('++1x1x+x1x')
    #print karvaToStandard('*+3-412')
   
    Data.populate() # create some new data points

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
    print 'Best: ', p.best, ' => ', karvaToStandard(p.best)

    if p.best.solved:
        print 'SOLVED! (should be x+x*x)'
