#diff eq rk2 time scan

from numpy import *

k = 0.1/60
ambient = 30
start = 100
end = 70

def DE(temp):
    DE = -k * (temp - ambient)
    return DE

for n in arange (-3,5,1):
    stepsize = float(10**(-float(n)))
    t = 0
    temp = start
    while temp:
        tmid = temp + (DE(temp) * stepsize * 0.5)
        newtemp = temp + (DE(tmid) * stepsize)
        t = t + stepsize
        temp = newtemp
        if temp <= end:
            t = t + (1/DE(tmid)) * (end - temp)
            break
    analytic = (-1/k) * log((end - ambient)/(start - ambient))
    error = abs(analytic - t)
    print(stepsize,error)