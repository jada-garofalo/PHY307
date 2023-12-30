#binary star system (and ternary)

from numpy import *

G = 4 * (pi ** 2)
dt = 10 ** (-3)
Ms1 = 2
Ms2 = 1.2
Ms3 = 1.4

v1 = array([0, 3, 0])
s1 = array([7, 0, 0])

v2 = array([-1, 0, 0])
s2 = array([1, -1, 0])

v3 = array([1, 0, 0])
s3 = array([0, 1, 0])

cmom = (Ms1 * v1 + Ms2 * v2 + Ms3 * v3) / (Ms1 + Ms2 + Ms3)
v1 = v1 - cmom
v2 = v2 - cmom
v3 = v3 - cmom

while True:
    s1 = s1 + (v1 * dt * 0.5)
    s2 = s2 + (v2 * dt * 0.5)
    s3 = s3 + (v3 * dt * 0.5)
    r12 = linalg.norm(s1 - s2)
    r23 = linalg.norm(s2 - s3)
    r13 = linalg.norm(s1 - s3)
    v1 = v1 - (G * (s1 - s2) * dt * Ms2 / (r12 ** 3)) - (G * (s1 - s3) * dt * Ms3 / (r13 ** 3))
    v2 = v2 - (G * (s2 - s1) * dt * Ms1 / (r12 ** 3)) - (G * (s2 - s3) * dt * Ms3 / (r23 ** 3))
    v3 = v3 - (G * (s3 - s2) * dt * Ms2 / (r23 ** 3)) - (G * (s3 - s1) * dt * Ms1 / (r13 ** 3))
    s1 = s1 + (v1 * dt * 0.5)
    s2 = s2 + (v2 * dt * 0.5)
    s3 = s3 + (v3 * dt * 0.5)
    print("C", 0.2, 0.03, 0.15)  # color one
    print("ct3", 0, s1[0], s1[1], s1[2], 0.1)  # orbit one
    print("C", 0.001, 0.001, 0.7)  # color two
    print("ct3", 1, s2[0], s2[1], s2[2], 0.1)  # orbit two
    print("C", 0.01, 0.01, 0.2)  # color three
    print("ct3", 2, s3[0], s3[1], s3[2], 0.1)  # orbit three
    print("F")  # flush

