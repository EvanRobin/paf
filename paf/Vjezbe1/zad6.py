import numpy as np
import matplotlib.pyplot as plt
import math
def circles(x,y,xc,yc,r):
    v=math.sqrt((x-xc)**2+(y-yc)**2)
    if r>v:
        print("Tocka je unutar kruznice")
    elif r==v:
        print("Tocka je na radijus kruznice")
    elif r<v:
        print("Tocka je izvan kruznice")
    phi = np.linspace(0, 2*np.pi, 200)
    xpl = r*np.cos(phi)+xc
    ypl = r*np.sin(phi)+yc
    plt.plot(xpl,ypl)
    plt.axis("equal")
    plt.plot(x, y, "s")
    plt.show()
circles(1,2,3,2,2)