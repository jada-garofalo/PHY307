#diff eq euler error code

from numpy import *

k = 0.1/60
ambient = 30
start = 100

def DE(temp):
    DE = -k * (temp - ambient)
    return DE

for n in arange (-3,7,1):
    stepsize = float(10**(-float(n)))
    t = 0
    temp = start
    for t in arange (0,300,stepsize):
        newtemp = temp + (DE(temp) * stepsize)
        temp = newtemp
        t = t
    analytic = ambient + ((start - ambient) * exp(-k * t))
    error = abs(analytic - temp)
    print(stepsize,error)