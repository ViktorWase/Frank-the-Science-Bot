"""
    This is a the template for the functions.

    So far we only have Artificial Neural Networks
    and Radial Basis Functions.

    All function classes need the methods described below.
"""
from tautology import *
import random


class radialBasisFunctionParameters:
    def __init__(self, chosenAttributes, ... ):
        """
            It doesn't matter much how the
            constructor looks like. But it
            probably needs the array chosenAttributes
            to tell if which attributes are used in
            the hypothesis.

            Make sure that it is called correctly from
            the hypothesis constructor.
        """

    def randomHypothesis(self, database):
        """
            This resets the parameters of the hypothesis
            to a bunch of random values.
        """

    def addRandomJump(self):
        """
            This adds a small mutation to the parameters
            of the hypothesis.
        """

    def functionName(x):
        """
            This method can be called whatever (But
            make sure it's called correctly from the
            function method in hypothesis.py)

            This should return a single value from the
            vector input x. This is the function that
            the object is representing.
        """

    def returnCopy(self):
        """
            This returns a copy of the object.
            Make sure to copy all vectors by value,
            and not by reference.
        """
    def getNeig_copy( self, database ):
        """
            This returns a copy of the object.
            (Make sure to copy all vectors by value,
            and not by reference.)
            It then adds a small random jump to
            the copied object.

        """
