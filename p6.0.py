#stellar orbit code

from numpy import *

#constants and relativistic conditions
G = 4 * (pi ** 2)
dt = 10 ** (-3)
eps = 0

#solar conditions
Ms = 1
xs = 0.2
ys = 0.3

#planetary conditions - for earth (2pi, 0, 0, 1)
vy = 2 * pi
vx = 0
y = 0
x = 1

while True:
    x = x + (vx * dt * 0.5)
    y = y + (vy * dt * 0.5)
    r = (((x - xs) ** 2) + ((y-ys) ** 2)) ** 0.5
    ax = -G * Ms * (x - xs) * (r ** (-3 - eps))
    ay = -G * Ms * (y - ys) * (r ** (-3 - eps))
    vx = vx + (ax * dt)
    vy = vy + (ay * dt)
    x = x + (vx * dt * 0.5)
    y = y + (vy * dt * 0.5)
    print("C", 0.001, 0.001, 0.7)  #star color
    print("c3", xs, ys, 0, 0.03 ) #star
    print("C", 0.2, 0.03, 0.15)  #orbit color
    print("ct3", 0, x, y, 0, 0.02) #orbit
    print("F") #flush
    E = 0.5 * ((vx ** 2) + (vy ** 2)) - (G * Ms * ((x ** 2) + (y ** 2)) ** (-0.5))
    K = 0.5 * ((vx ** 2) + (vy ** 2))
    U = -G * Ms * (((x ** 2) + (y ** 2)) ** (-0.5))
    print("C", 0.3, 0.1, 0.3)  #text color
    print("T", 0.45, -0.4)
    print("Total Energy", E)
    print("T", 0.45, -0.45)
    print("Kinetic Energy", K)
    print("T", 0.45, -0.5)
    print("Potential Energy", U)
