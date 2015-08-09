"""
    This is a tempalte for the functions that takes
    the database and choses some set of the attributes.

    The general idea is that it should find some set of
    attributes that are correlated. These are then sent
    to some part of the optimization algorithm to find
    a function that describes their correlation.
"""

def choiceFunction(database, numberOfAttributesInDatabase):
    """
        It takes the database and an int and returns a bool
        array of lenght numberOfAttributesInDatabase. I

        If the output array is true at index x, it means
        that attribute x is used in the function. Otherwise
        it isn't.

        These function should replace chooseAttributes in scienceFunctions.py
    """
