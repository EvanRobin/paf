import numpy as np
import matplotlib.pyplot as plt
def force(F,m):
    v=[0]
    s=[0]
    t=np.linspace(0,10,101)
    a=F/m
    dt=0.1
    for i in range(0,100,1):
        v.append(v[-1]+dt*a) 
        s.append(s[-1]+dt*v[-1])
    
    plt.plot(t, np.repeat(a, 101))
    plt.xlabel("t(s)")
    plt.ylabel("a(m/s2)")
    plt.show()

    plt.plot(t, v)
    plt.xlabel("t(s)")
    plt.ylabel("v(m/s)")
    plt.show()

    plt.plot(t, s)
    plt.xlabel("t(s)")
    plt.ylabel("a(m)")
    plt.show()
    

    plt.show()
force(10,1)