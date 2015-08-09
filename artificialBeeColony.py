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
    def __init__(self, database, hypothesis, isEmployed):
        """
            Constructor for bees.

            The three first arguments are functions that define the optimization
            problem.
            The last one either sets is to an onlooker or an employed bee.
        """
        c1 = 1.0

        self.database = database
        if(isEmployed):
            #self.generateHypothesis = generateHypothesis
            #self.bestFoodSource = generateHypothesis(len(database.datapoints[0].attributes),self.database)
            #self.addRandomLittleJump = addRandomLittleJump
            #self.fitnessOfHypothesis = fitnessOfHypothesis
            self.hypothesis = hypothesis
            self.valueOfBestFoodSource = self.hypothesis.updateAndReturnFitness( database, c1)

            #self.getHypObj = getHypObj

            self.isEmployed = True
        else:
            #self.generateHypothesis = generateHypothesis
            #self.bestFoodSource = None
            #self.addRandomLittleJump = addRandomLittleJump
            #elf.fitnessOfHypothesis = fitnessOfHypothesis
            #self.valueOfBestFoodSource = -10000000000000000000000
            self.hypothesis = hypothesis
            #self.getHypObj = getHypObj
            #self.hypothesis.fitness = -100000000000000000000000000000

            self.isEmployed = False

    def goScouting(self):
        #self.bestFoodSource = self.generateHypothesis(len(self.database.datapoints[0].attributes),self.database)
        #self.valueOfBestFoodSource = self.fitnessOfHypothesis(self.database, self.bestFoodSource)
        self.hypothesis.getRandom(self.database)

    def isEmployed(self):
        if(self.isEmployed == True):
            return True
        else:
            return False

    def dance(self):
        return self.hypothesis.getFitness()

    def chooseAnEmployedBeeToFollow(self, dancingList, colony):
        """
            Goes through a fourth (ish) of the dancingList
            and picks the best one.
            If they're all worse than the one the bee has
            in memory, it does nothing.
        """
        for i in range(int(len(dancingList)/4)):
            index = random.randint(0, len(dancingList)-1)
            bestIndex = -1
            if dancingList[index]>self.hypothesis.getFitness():
                bestIndex = index

            if (bestIndex != -1):
                self.hypothesis = colony[index].hypothesis.returnCopy()
                self.hypothesis.updateAndReturnFitness(self.database, 1.0)
                #self.hypothesis = colony[index].hypothesis

    def checkNeighbour(self):
        """
            Checks if a food source close by is better. If it is better
            the bee goes there instead.
        """
        self.hypothesis.checkNeighbour(self.database)

        #neighbour = self.addRandomLittleJump(list(self.bestFoodSource))
        #valueOfNeighbour = self.fitnessOfHypothesis(self.database, neighbour)
        #if(valueOfNeighbour > self.valueOfBestFoodSource):
        #    self.valueOfBestFoodSource = valueOfNeighbour
        #    self.bestFoodSource = neighbour

class Colony:
    """
        This is a colony of Bees.
    """
    def __init__(self, database, numOfEmployedBees, numOfOnlookers, getRandomHypothesisObj):
        self.colony = []
        self.dancingList = []
        self.size = numOfOnlookers + numOfEmployedBees
        self.numOfEmployedBees = numOfEmployedBees
        self.numOfOnlookers = numOfOnlookers

        self.database = database

        for i in range(numOfEmployedBees):
            hyp = getRandomHypothesisObj( self.database )
            hyp.updateAndReturnFitness(self.database, 1.0)

            bee = Bee(database, hyp, True)
            self.colony.append(bee)

        for i in range(numOfOnlookers):
            hyp = getRandomHypothesisObj( self.database )
            bee = Bee(database, hyp, False)
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
            if(minVal > bee.hypothesis.getFitness()):
                minVal = bee.hypothesis.getFitness()
            meanVal = meanVal + bee.hypothesis.getFitness()

        meanVal = meanVal / self.numOfEmployedBees

        for bee in self.colony[0:self.numOfEmployedBees]:
            if( bee.hypothesis.getFitness() < minVal + (meanVal-minVal)/2 ):
                bee.goScouting()

    def bestBee(self):
        """
            Returns the best bee.
        """
        maxVal = -10000000000000000000
        bestBee = None
        for bee in self.colony:
            bee.hypothesis.updateAndReturnFitness(self.database, 1.0)
            if(bee.hypothesis.getFitness() > maxVal):
                maxVal = bee.hypothesis.getFitness()
                bestBee = bee
        return bestBee

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
            print self.bestBee().hypothesis.getFitness()
            #print self.colony[0].fitnessOfHypothesis(self.database, self.bestBee())
            #print ""
        return self.bestBee().hypothesis

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
#colony = Colony(20,20, hyp, mutate, fit)
#bestSolution = colony.findBestFlower(500)
#print "x: ",
#rint bestSolution
#print "Fitness(x): ",
#print fit(bestSolution)
