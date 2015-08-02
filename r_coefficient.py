import math

def pearson_r_correlation(X, Y):
    """
        Takes 2 vectors (of equal length) and
        finds the (linear) correlation between
        the 2 variables.

        Everything is stolen from here:
        https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
    """

    n = len(X)

    x_mean = 0
    for x in X:
        x_mean += x
    x_mean = x_mean/n

    y_mean = 0
    for y in Y:
        y_mean += y
    y_mean = y_mean/n

    r = 0
    for index in range(n):
        r += (X[index]-x_mean)*(Y[index]-y_mean)

    tmp = 0
    for index in range(n):
        tmp += (X[index]-x_mean)**2
    r = r/math.sqrt(tmp)

    tmp = 0
    for index in range(n):
        tmp += (Y[index]-y_mean)**2
    r = r/math.sqrt(tmp)

    return r
