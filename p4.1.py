#diff eq rk2 error code

from numpy import *

k = 0.1/60
ambient = 30
start = 100

def DE(temp):
    DE = -k * (temp - ambient)
    return DE

for n in arange (-3,5,1):
    stepsize = float(10**(-float(n)))
    t = 0
    temp = start
    tmax = 300
    for t in arange (0,tmax - (stepsize/2),stepsize):
        tmid = temp + (DE(temp) * stepsize * 0.5)
        newtemp = temp + (DE(tmid) * stepsize)
        temp = newtemp
    analytic = ambient + ((start - ambient) * exp(-k * tmax))
    error = abs(analytic - temp)
    print(stepsize,error)