import pandas as pd
import numpy as np

def gini(x):
    """Calculate the Gini coefficient for series of observed values (x). 
    where:
    * x is the array of observed values (and all x are positive, non-zero values)
      Note: x must be a numpy array or a pandas series
    See: https://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    """
    
    # - sanity checks
    if not isinstance(x, pd.Series) and not isinstance(x, np.ndarray):
        raise TypeError('input series must be a pandas Series or a numpy ndarray')
    if x.min() <= 0:
        raise ValueError('all input values in series must be positive and non-zero')

    # let's work with numpy arrays
    if isinstance(x, pd.Series):
        x = x.to_numpy()
        
    # sort values in ascending order
    x = np.sort(x)

    # n is the number of values observed
    n = len(x)
        
    # i is the rank of the x-values when sorted in ascending order
    i = np.arange(1, n+1)
    
    # - calculate the Gini coefficient
    return ((2 * i - n - 1) * x).sum() / (n * x.sum())
    
    
# An alternate approach ...
def gini2(x):
    """ Calculate Gini from observed values using summation-as-integration """
    
    if not isinstance(x, pd.Series) and not isinstance(x, np.ndarray):
        raise TypeError('input series must be a pandas Series or a numpy array')
    if x.min() <= 0:
        raise ValueError('all input values in series must be positive and non-zero')

    # let's work with numpy arrays
    if isinstance(x, pd.Series):
        x = x.to_numpy()
    
    # calculate the line-of-equality and the lorenz curve
    lorenz = np.sort(x).cumsum()
    height = lorenz[-1]
    n = len(lorenz)
    equality = np.arange(1, n+1) * height / n
    
    # calculate Gini
    A_area = (equality - lorenz).sum() # area between lorenz and equality
    AB_area = n * height / 2 # area of triangle
    return A_area / AB_area
