import numpy as np
import math
import matplotlib.pyplot as plt
import projectile as pr
p1=pr.Fric()
m=6
vx=0
vy=0
p=1.225
cd=0.5
A=1
dt=0.0005
p1.set_initial_conditions(0,0,30,10,cd,A,p,m)
print(p1.cred(dt))
plt.plot(p1.checkx(),p1.checky())
plt.show()
