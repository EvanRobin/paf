import module
import math
import numpy as np
import matplotlib.pyplot as plt
dx=0.01
def f2(x):
    return math.sin(x)
def derive_dot2(f,x):
    return (module.value(f,x)-module.value(f,x-dx))/dx
def derive_dot3(f,x):
    return (module.value(f,x+dx)-module.value(f,x-dx))/2*dx
def derivitives(f,a,b,option):
    d=[]
    ab=np.linspace(a,b,50)
    if option:
        for i in ab:
            d.append(derive_dot3(f,i))
    else:
        for i in ab:
            d.append(derive_dot2(f,i))
    return d

def intagral_a(f,a,b,steps):
    inta=[]
    fu=0
    fl=0
    lx=np.linspace(a,b,steps+1)
    for i in range (0,steps,1):
        fl+=module.value(f,lx[i])*(b-a)/steps
        fu+=module.value(f,lx[i+1])*(b-a)/steps
    return fl,fu
def intagral_b(f,a,b,steps):
    fl=0
    tr=0
    lx=np.linspace(a,b,steps+1)
    for i in range (0,steps,1):
        fl+=module.value(f,lx[i])*(b-a)/steps
        tr+=((b-a)/steps*(abs(module.value(f,lx[i+1])-module.value(f,lx[i]))))/2
    return tr+fl