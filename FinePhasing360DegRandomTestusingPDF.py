# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 06:40:24 2021

@author: bob
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.stats import distributions
from scipy.stats import norm
import statistics
#import scipy
from IPython.display import display, Math
#from scipy._lib._bunch import _make_tuple_bunch
#LinregressResult = _make_tuple_bunch('LinregressResult',
#                                     ['slope', 'intercept', 'rvalue',
#                                      'pvalue', 'stderr'],
#                                     extra_field_names=['intercept_stderr'])

Energy=1500  #Energy=[250,750,1500]
Dispersion = 0.47  #Dispersion = [0.275,0.443,0.47]
reSolution = 30e-6  #reSolution=[25e-6,25e-6,30e-6]

def test_func(x, amp, omega, phi):
    return amp*np.cos(omega * x + phi)

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

def fitOut(offSet):
    degRees = []
    outPut=[]
    for i in range(-180,190,20):
       #point=-16*math.cos(math.radians(offSet-90+i))+16*math.cos(math.radians(offSet+90+i))
            plusNinety=(16*math.cos(math.radians(offSet+i))*Dispersion)/Energy + (np.random.rand()-0.5)*reSolution
            #plusNinety=(16*math.cos(math.radians(offSet+i))*Dispersion)/Energy 
            point = truncate(plusNinety,5)
            degRees.append(math.radians(i))
            outPut.append(point)   
    params, params_covariance = optimize.curve_fit(test_func, degRees, outPut, p0=[.017, 1, 0])
    #print (math.degrees(params[2]))
    
    #plt.plot(degRees,outPut)
    #plt.xlabel('zero crossing at '+str(-c))
    #plt.show()
    return (math.degrees(params[2]))

if __name__ == "__main__":
    lineOut=[]
    deltaDeg=[]
    zeroCross=[]
    for i in range(0,10000):
        tempPhase=0
        deltaDeg.append(tempPhase)
        zeroCross.append(fitOut(tempPhase))
    
    
    plt.scatter(zeroCross,norm.pdf(zeroCross))
    #print(slope, intercept, r, slope_stderr, intercept_stderr)
    print(statistics.stdev(zeroCross))
    
    #plt.xlabel('Std.Dev is '+str(norm.std))
    #plt.plot(deltaDeg, lineOut, label='fitted line')
    plt.show()
        
    

        