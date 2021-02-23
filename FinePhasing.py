# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 06:40:24 2021

@author: bob
"""

import math
import numpy as np
import matplotlib.pyplot as plt
Energy=1500  #Energy=[250,750,1500]
Dispersion = 0.47  #Dispersion = [0.275,0.443,0.47]
reSolution = 30e-6  #reSolution=[25e-6,25e-6,30e-6]


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
    for i in range(-5,6,1):
       #point=-16*math.cos(math.radians(offSet-90+i))+16*math.cos(math.radians(offSet+90+i))
            plusNinety=round(((16*math.cos(math.radians(offSet+90+i))*Dispersion)/Energy)/reSolution,0)*reSolution
            minusNinety=round(((-16*math.cos(math.radians(offSet-90+i))*Dispersion)/Energy)/reSolution,0)*reSolution
            point = truncate(minusNinety,5) + truncate(plusNinety,5)
            degRees.append(i)
            outPut.append(point)   
    y=np.array(degRees)
    x=np.array(outPut)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return c
    



    #plt.plot(degRees,outPut)
    #plt.xlabel('zero crossing at '+str(-c))
    #plt.show()
    
if __name__ == "__main__":
    deltaDeg=[]
    zeroCross=[]
    for i in range(0,10000):
        tempPhase=(i-5000)/1000
        deltaDeg.append(tempPhase)
        zeroCross.append(fitOut(tempPhase))
    plt.plot(deltaDeg,zeroCross)
    plt.show()
        