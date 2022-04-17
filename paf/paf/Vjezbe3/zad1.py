import Particle as pa
import numpy as np
import math
import matplotlib.pyplot as plt
p1=pa.Particle()
p1.set_initial_conditions(0,0,10,60)
vx=10*np.cos(60*np.pi/180)
vy=10*np.sin(60*np.pi/180)
#t=(vy+math.sqrt(vy**2))/9.81
#print("Analiticki:",vx*t)
#print("Numericki:",p1.range())
delta=3
an=vx*3
numer=[]
dt=1
err=[]
tl=[]
times=0
for i in range (0,99,1):    
    dt+=-0.01
    tl.append(dt)
    p1.reset()
    p1.set_initial_conditions(0,0,10,60,dt)
    
    err.append(abs(an-p1.range_deltat(delta))/an)
plt.plot(tl,err)
plt.show()
    
