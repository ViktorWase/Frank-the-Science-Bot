"""
    The artificialBeeColony function creates a lot of
    bees that then minimizes a function.
"""

import math
import random

class Bee:
    """
        These bees try to find the best food source (which is a minima
        of the error function).
    """
    def __init__(self, generateHypothesis, addRandomLittleJump, fitnessOfHypothesis, isEmployed):
        """
            Constructor for bees.

            The three first arguments are functions that define the optimization
            problem.
            The last one either sets is to an onlooker or an employed bee.
        """
        if(isEmployed):
            self.generateHypothesis = generateHypothesis
            self.bestFoodSource = generateHypothesis()
            self.addRandomLittleJump = addRandomLittleJump
            self.fitnessOfHypothesis = fitnessOfHypothesis
            self.valueOfBestFoodSource = fitnessOfHypothesis(self.bestFoodSource)

            self.isEmployed = True
        else:
            self.generateHypothesis = generateHypothesis
            self.bestFoodSource = None
            self.addRandomLittleJump = addRandomLittleJump
            self.fitnessOfHypothesis = fitnessOfHypothesis
            self.valueOfBestFoodSource = 0

            self.isEmployed = False

    def goScouting(self):
        self.bestFoodSource = self.generateHypothesis()
        self.valueOfBestFoodSource = self.fitnessOfHypothesis(self.bestFoodSource)

    def isEmployed(self):
        if(self.isEmployed == True):
            return True
        else:
            return False

    def dance(self):
        return self.valueOfBestFoodSource

    def chooseAnEmployedBeeToFollow(self, dancingList, colony):
        """
            Goes through a tenth (ish) of the dancingList
            and picks the best one.
            If they're all worse than the one the bee has
            in memory, it does nothing.
        """
        for i in range(int(len(dancingList)/10)):
            index = random.randint(0, len(dancingList)-1)
            if dancingList[index]>self.valueOfBestFoodSource:
                self.bestFoodSource = colony[index].bestFoodSource
                self.valueOfBestFoodSource = colony[index].valueOfBestFoodSource

    def checkNeighbour(self):
        """
            Checks if a food source close by is better. If it is better
            the bee goes there instead.
        """
        neighbour = self.addRandomLittleJump(self.bestFoodSource)
        valueOfNeighbour = self.fitnessOfHypothesis(neighbour)
        if(valueOfNeighbour > self.valueOfBestFoodSource):
            self.valueOfBestFoodSource = valueOfNeighbour
            self.bestFoodSource = neighbour

def test(w):
    #THIS IS SHOULD BE A PROPER FITNESS FUNCTION! FIX!
    return sum(abs(w))

class Colony:
    """
        This is a colony of Bees.
    """
    def __init__(self, numOfEmployedBees, numOfOnlookers, randomHypothesis, addRandomLittleJump, fitnessOfHypothesis):
        self.colony = []
        self.dancingList = []
        self.size = numOfOnlookers + numOfEmployedBees
        self.numOfEmployedBees = numOfEmployedBees
        self.numOfOnlookers = numOfOnlookers

        for i in range(numOfEmployedBees):
            bee = Bee(randomHypothesis, addRandomLittleJump, fitnessOfHypothesis, True)
            self.colony.append(bee)

        for i in range(numOfOnlookers):
            bee = Bee(randomHypothesis, addRandomLittleJump, fitnessOfHypothesis, False)
            self.colony.append(bee)


    def lookForFlowers(self):
        """
            The employed bees checks if there are any better flowers
            near-by.
        """
        for bee in self.colony[0:self.numOfEmployedBees]:
            if(bee.isEmployed == False):
                print "Error in 'lookForFlowers()'"
            else:
                bee.checkNeighbour()

    def dancing(self):
        """
            All the employed bees dance their little dance to
            show the other bees how good their food source is.
        """
        self.dancingList = []
        for bee in self.colony[0:self.numOfEmployedBees]:
            if(bee.isEmployed == False):
                print "Error in 'dancing()'"
            else:
                self.dancingList.append(bee.dance())

    def lookAtTheDance(self):
        """
            All the omlookers looks at the dance of the employed
            bees and chooses to squat at a nice food source.
        """
        for bee in self.colony[self.numOfEmployedBees:self.size]:
            if(bee.isEmployed == True):
                print "Error in 'lookAtTheDance()'"
            else:
                bee.chooseAnEmployedBeeToFollow(self.dancingList, self.colony)

    def selectScouts(self):
        """
            Takes all employed bees whose food source is
            lower than halfway between the minimnum and the
            mean, and tells them to go scoutning.
        """
        meanVal = 0
        minVal = 10000000000000
        for bee in self.colony[0:self.numOfEmployedBees]:
            if(minVal > bee.valueOfBestFoodSource):
                minVal = bee.valueOfBestFoodSource
            meanVal = meanVal + bee.valueOfBestFoodSource

        meanVal = meanVal / self.numOfEmployedBees

        for bee in self.colony[0:self.numOfEmployedBees]:
            if( bee.valueOfBestFoodSource < minVal + (meanVal-minVal)/2 ):
                bee.goScouting()

    def bestBee(self):
        """
            Returns the best bee.
        """
        maxVal = -1
        bestBee = None
        for bee in self.colony:
            if(bee.valueOfBestFoodSource > maxVal):
                maxVal = bee.valueOfBestFoodSource
                bestBee = bee
        return bee.bestFoodSource

    def doAnItteration(self):
        """
            This combines all parts of the search.
        """
        self.lookForFlowers()
        self.dancing()
        self.lookAtTheDance()
        self.selectScouts()

    def findBestFlower(self, maxNumberOfItterations):
        """
            Call this function from outside. It optimizes the
            shit out of the stuff in the scienceFunctions.py file.
        """
        for itteration in range(maxNumberOfItterations):
            self.doAnItteration()
            #print self.bestBee()
            #print ""
        return self.bestBee()

#These are just example functions. Use the fancy ones
#from scienceFunction.py instead.
def fit(x):
    #This is just a function with a lot of local
    #optimas.
    return abs(math.sin(x/3)*(math.sqrt(x+6))/x)
def hyp():
    #A first guess at a good solution
    return random.random()*10000
def mutate(x):
    #Add a little jump.
    return x+random.random()-0.5

#How you start it.
colony = Colony(20,20, hyp, mutate, fit)
bestSolution = colony.findBestFlower(500)
print "x: ",
print bestSolution
print "Fitness(x): ",
print fit(bestSolution)
