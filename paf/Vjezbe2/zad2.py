import numpy as np
import matplotlib.pyplot as plt
def hor_hit(vo,a):
    g=-9.8
    t=np.linspace(0,10,101)
    dt=0.1
    x=[0]
    y=[0]
    vx=vo*np.cos(a*np.pi/180)
    vy=[vo*np.sin(a*np.pi/180)]
    for i in range(0,100,1):
        x.append(x[-1]+dt*vx)        
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+dt*vy[-1])
    

    plt.plot(x, y)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.show()
    
    plt.plot(t, x)
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.show()

    plt.plot(t, y)
    plt.xlabel("t(s)")
    plt.ylabel("y(m)")
    plt.show()
hor_hit(100,45)



