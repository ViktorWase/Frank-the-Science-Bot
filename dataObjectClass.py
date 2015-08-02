class dataObject:
    """
        Each of the data points in the database
        should be represented as one of these objects.
        The actual data is put in the attributes vector.
    """
    def __init__(self, numberOfAttributes):

        self.attributes = [0.0]*numberOfAttributes

    def setAttributes(self, attributesIn):
        for index in range(len(attributesIn)):
            self.attributes[index] = attributesIn[index]

class Database:
    """
        A container class for the dataObjects.
    """
    def __init__(self, database_in):
        self.datapoints = database_in
        self.numElements = len(database_in)
        self.numAttributes = len(database_in[0].attributes)

        self.pureData = [0.0]*self.numElements*self.numAttributes

        index = 0
        for element in range(self.numElements):
            for attribute in range(self.numAttributes):
                self.pureData[index] = self.datapoints[element].attributes[attribute]
                index += 1

    def getVectorWithAttributeNr(self, x):
        return list(self.pureData[x*self.numAttributes:(x+1)*self.numAttributes])
