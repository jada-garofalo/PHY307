#gaussian integral code

from numpy import *

Rs = 0 #defining the variable to start at 0
r = 0 #defining the variable to start at 0
stepsize = 0.00001

def f(x):
    f = exp(-1 * x**2) #this segment defines our function
    return f #this part solved my issue, as it returns a number rather than a func

for x in arange(-20,20,stepsize): #(lower bound, upper bound, stepsize)
    F = f(x)
    r = F * stepsize #interprets area as a function of stepsize and function output
    Rs = Rs + r #this acts as a summation for our outputted areas
    print(r) #this lets me keep track that the individual areas are being computed alright

print("The integral of f(x) over the given range is",Rs)