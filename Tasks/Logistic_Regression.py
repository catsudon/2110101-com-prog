import numpy as np

def p( X ): 
    logistic_regression = X[::,0]*0.1+X[::,1]*0.5-3.98
    sigmoid = 1/(1+np.e**-logistic_regression[::])
    return sigmoid

exec(input().strip())