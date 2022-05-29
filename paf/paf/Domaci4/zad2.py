import numpy as np
import math
import matplotlib.pyplot as plt
import projectile as pr
p1=pr.Fric()
m=1
p=1.225
cd=0.5
A=1
dt=0.0005
angle=0
for i in range (0,100,1):
    angle+=1 
    p1.set_initial_conditions(0,0,angle,10,cd,A,p,m)   
    if p1.meta(8,8,100):
        plt.plot(p1.checkx,p1.checky)        
    p1.reset()
plt.show()