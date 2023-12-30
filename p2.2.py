#prime finder code

from numpy import *

N = int(input("Enter an integer to see how many prime numbers are less than or equal to your integer:       "))

def pi(N):
    return N/log(N)

print("The Prime Number Theorem suggests that our number should be somewhere in the neighborhood of",pi(N))

nprime = 0
scan = 0

for x in arange(1,N+1,1):
    if x == 2:
        scan = 1
    for y in arange(2,x/2+1,1):
            if (x % 2 == 0):
                scan = 0
                break
            if (x % y == 0):
                scan = 0
                break
            else:
                scan = 1

    if scan == 1:
        print(x)
    nprime = nprime + scan

print("The actual number of primes is", nprime)