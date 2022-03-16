import numpy as np
import matplotlib.pyplot as plt
def force(F,m):
    v=[0]
    s=[0]
    t=np.linspace(0,10,10)
    a=F/m
    for i in range(1,10,1):
        v.append(v[i-1]+1*a) 
        s.append(s[i-1]+1*v[i])
    fig, axs = plt.subplots(3)
    axs[0].plot(t, np.repeat(a, 10))
    axs[1].plot(t, v)
    axs[2].plot(t, s)

    plt.show()
force(10,1)