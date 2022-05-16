from asyncio import constants
import numpy as np
import math
import matplotlib.pyplot as plt
import projectile as pr
p1=pr.Fric()
alpha=30
vx=0
vy=0
v=10
p=1.225
A=1
dt=0.01
CD=0.5
MASS=1

ma = []
rM = []
cd = []
rcd = []

for m in np.arange(0.5, 50.5, 5):
    ma.append(m)
    p1.set_initial_conditions(0,0,alpha,v,CD,A,p,m) 
    rM.append(p1.rangeRK4())
    rcd.append(p1.dom())
    p1.reset()
    
for c in np.arange(0.1, 1.1, 0.1):
    cd.append(c)
    p1.set_initial_conditions(0,0,alpha,v,c,A,p,MASS) 
    p1.rangeRK4()
    rcd.append(p1.dom())
    print(p1.dom)
    p1.reset()
print(rM)