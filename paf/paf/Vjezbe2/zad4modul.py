import matplotlib.pyplot as plt
import numpy as np
import math
def kosi(v,a):
    g=-9.81
    dt=0.1
    x=[0]
    y=[0]
    t=[0]
    vx=v*np.cos(a*np.pi/180)
    vy=[v*np.sin(a*np.pi/180)]
    while y[-1]>=0:
        x.append(x[-1]+dt*vx)        
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+dt*vy[-1])
        t.append(t[-1]+dt)
    plt.plot(x, y)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.show()
def max(v,a):
    ma=0
    g=-9.81
    dt=0.1
    x=[0]
    y=[0]
    t=[0]
    vy=[v*np.sin(a*np.pi/180)]
    while y[-1]>=0:       
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+dt*vy[-1])
        t.append(t[-1]+dt)
    for i in y:
        if i > ma:
            ma=i
    print(ma)
def domet(v,a):
    g=-9.81
    dt=0.1
    x=[0]
    y=[0]
    t=[0]
    vx=v*np.cos(a*np.pi/180)
    vy=[v*np.sin(a*np.pi/180)]
    while y[-1]>=0:
        x.append(x[-1]+dt*vx)        
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+dt*vy[-1])
        t.append(t[-1]+dt)
    print(x[-1])

def max_speed(v,a):
    ma=0
    g=-9.81
    dt=0.1
    x=[0]
    y=[0]
    t=[0]
    vx=v*np.cos(a*np.pi/180)
    vy=[v*np.sin(a*np.pi/180)]
    while y[-1]>=0:
        x.append(x[-1]+dt*vx)        
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+dt*vy[-1])
        t.append(t[-1]+dt)
    for i in vy:
        if i > ma:
            ma=i
    print(math.sqrt(ma**2+vx**2))
def meta(v,a,xm,ym,r):
    g=-9.81
    x=[0]
    y=[0]
    vx=v*np.cos(a*np.pi/180)
    vy=[v*np.sin(a*np.pi/180)]
    tm=np.linspace(0,xm/vx,100)
    dt=tm/100
    for i in range(0,100,1):
        vy.append(vy[-1]+dt*g)
        y.append(y[-1]+vy[-1]*dt)    