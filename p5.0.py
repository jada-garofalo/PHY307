#pendulum animation code

from numpy import *

dt = 1
L = 1
g = 9.81
anaperiod = 2 * pi * ((L / g) ** 0.5)

while dt > (10 ** -6):
    numperiod = 0
    t = 0
    omega = 0
    alpha = 0
    dt = dt / 10
    theta = 2 * dt
    while True:
        alpha = (-g / L) * sin(theta)
        theta = theta + (omega * dt * 0.5)
        omega = omega + (alpha * dt)
        theta = theta + (omega * dt * 0.5)
        #x = L * cos(theta)
        #y = L * sin(theta)
        t = t + dt
        #print ("c", -y, -x, 0.02) #circle
        #print ("C", 0.2, 0.1, 0.1) #color
        #print ("l", 0, 0, -y, -x) #line
        #print ("F") #flush
        #print (t, theta)
        #print (t, omega)
        if omega > 0:
            numperiod = 2 * t
            fracdev = abs(numperiod - anaperiod) / anaperiod
            theta = abs(theta)
            print(theta, fracdev)
            break
