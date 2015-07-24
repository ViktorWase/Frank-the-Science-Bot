class dataObject(object):
    """
        Each of the data points in the database
        should be represented as one of these objects.
        The actual data is put in the attributes vector.
    """
    def __init__(self, numberOfAttributes):
        self.attributes = [0.0]*numberOfattributes

    def setAttributes(self, attributesIn):
        for index in range(len(attributesIn)):
            self.attributes[index] = attributesIn[i]