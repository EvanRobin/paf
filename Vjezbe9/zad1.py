import numpy as np
import math
import matplotlib.pyplot as plt
import bungee as pr
p1=pr.Bung()
p2=pr.Bung()
m=6
vy=0
p=1.225
cd=0.5
A=1
dt=0.0005
l=10
p1.set_initial_conditions(0,0,cd,A,p,m,l)
p1.weee_NO_FRICTION(20)
plt.plot(p1.checkt(),p1.checky())
p2.set_initial_conditions(0,0,cd,A,p,m,l)
p2.weee(20)
plt.plot(p2.checkt(),p2.checky())
plt.show()
plt.plot(p1.checkt(),p1.checkEel())
plt.plot(p1.checkt(),p1.checkEg())
plt.plot(p1.checkt(),p1.checkEki())
plt.plot(p1.checkt(),p1.checkEUK())
plt.show()
plt.plot(p2.checkt(),p2.checkEel())
plt.plot(p2.checkt(),p2.checkEg())
plt.plot(p2.checkt(),p2.checkEki())
plt.plot(p2.checkt(),p2.checkEUK())
plt.show()



