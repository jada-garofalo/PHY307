from numpy import *

image = 1  #0 for |less or plot, 1 for |anim
N = 10 ** 2 #number of connections
A = 10 ** 0.5 #amplitude
dt = 10 ** (-3)  #timestep
t = 0  #initial time lol

while True:
    m0 = 16 #string mass
    alpha = 2 #stiffness
    L0 = 1 #unstretched length
    L = 4 #stretched length

    mu = m0 / L #linear density
    m = L * mu / (N + 1) #mass of comp
    r0 = L0 / N #unstretched spring distance
    k = N * alpha / L0 #k per spring
    kbar = alpha / L0 #k over string
    T = kbar * (L - L0) #tension

    s = 0 #start condition
    nmode = 4 #normal mode
    sigma = 0.5 #fwhh

    position = zeros((N + 1, 2))
    velocity = zeros((N + 1, 2))

    for i in range(N+1):
        position[i, 0] = L/N * i

    if s == 0:
        for j in range(50, 51): #knife start position
            position[j, 1] = 2
    if s == 1:
        for j in range(1, N): #sinusoidal start position with period tracking
            position[j, 1] = A * sin(nmode * pi * position[j, 0] / L)
            tauTheory = 2 * L * (1 / nmode) * ((mu / T) ** 0.5)
    if s == 2:
        for j in range(1, N): #gaussian start position
            position[j, 1] = A * exp(-((position[j, 0] - 2) ** 2) / (sigma ** 2))

    while True:
        for i in range(1, N):
            position[i] = position[i] + velocity[i] * dt * 0.5
        for i in range(1, N):
            ri1 = linalg.norm(position[i] - position[i-1])
            ri2 = linalg.norm(position[i+1] - position[i])
            velocity[i] = velocity[i] + ((k * (ri1 - r0) * (position[i-1] - position[i]) / ri1) + (k * (ri2 - r0) * (position[i+1] - position[i]) / ri2)) * dt / m
        for i in range(1, N):
            position[i] = position[i] + velocity[i] * dt * 0.5
        if s == 1:
            if image == 0:
                coolN = int(N / (nmode * 2))
                coolV = velocity[coolN, 1]
                if coolV > 0:
                    tauReal = 2 * t
                    fracdiff = float(abs(tauTheory - tauReal) / tauReal)
                    print(A, fracdiff)
                    break
                t = t + dt
        if image == 1:
            for i in range(N+1):
                print("c", position[i, 0], position[i, 1], 0.01)
                if N > i:
                    print("l", position[i, 0], position[i, 1], position[i+1, 0], position[i+1, 1])
            print("F")
        if image == 0:
            A = A * 10
            if A > (10 ** -1):
                break
