import numpy as np
import matplotlib.pyplot as plt
def hor_hit(vo,a):
    g=-9.8
    t=np.linspace(0,10,11)
    x=[0]
    y=[0]
    vx=vo*np.cos(a*np.pi/180)
    vy=[vo*np.sin(a*np.pi/180)]
    for i in range(1,11,1):
        x.append(x[i-1]+1*vx)        
        vy.append(vy[i-1]+1*g)
        y.append(y[i-1]+1*vy[i])
    fig, axs = plt.subplots(3)
    axs[0].plot(x, y)
    axs[1].plot(t, x)
    axs[2].plot(t, y)

    plt.show()
    

hor_hit(10,45)



