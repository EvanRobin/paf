
import matplotlib.pyplot as plt
import MODULE as gib
import matplotlib.pyplot as plt
import numpy as np
def ks(x, v, t):
    return 5
def es(x, v, t):
    return -5*x
def xds(x, v, t):
    return 2*x - 3*v*t
g1 = gib.Force()
g1.set_in_conditions(5, 5, 1, es, 10)
t, x, v, a = g1.gibanje()
plt.plot(t, x)
plt.grid()
plt.show()
plt.plot(t, v)
plt.grid()
plt.show()
plt.plot(t, a)
plt.grid()
plt.show()