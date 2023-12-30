#numeric integration error code
# example given is looking at the square root of x from 1 to 2, trapezoid-style (with step-size binary error accounted for)

from numpy import *

integral = 0

def f(val):
    return x**(0.5)

def lrsec(lbound,stepsize):
    lrsec = f(lbound) * stepsize
    return lrsec

def rrsec(lbound,stepsize):
    rrsec = f(lbound + stepsize) * stepsize
    return rrsec

def trsec(lbound,stepsize):
    trsec = (f(lbound) + f(lbound + stepsize)) * 0.5 * stepsize
    return trsec

def mrsec(lbound,stepsize):
    mrsec = (f(lbound + (stepsize * 0.5))) * stepsize
    return mrsec

for n in arange (0,8,1):
    stepsize = float(10**(-float(n)))
    left = 1
    right = 2 - (stepsize / 2)
    exact = ((2 / 3) * (right ** (3 / 2))) - ((2 / 3) * (left ** (3 / 2)))
    for x in arange (left,right,stepsize):
        integral = integral + trsec(x,stepsize)
    error = abs(exact - integral)
    print(stepsize,error)
    integral = 0