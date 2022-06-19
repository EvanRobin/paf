import calcules as ca
import math
import numpy as np
import matplotlib.pyplot as plt
import module
def f2(x):
    return math.sin(x)
def f1(x):
    return x
def f3(x):
    return (1/2)*(x**2)
def f4(x):
    return 1*math.cos(x)
print(ca.derivitives(f2,0,1,1),np.linspace(0,1,50))
print(ca.derive_dot2(f2,1))

