import numpy as np
import math
import matplotlib.pyplot as plt
import projectile as pr
p1=pr.Fric()
p2=pr.Fric()
p=1.225
p1.set_initial_conditions_CUBE(60,10,1,p,1)
p2.set_initial_conditions_SPHERE(60,10,0.5,p,1)
p1.rangeRK4()
plt.plot(p1.checkx(),p1.checky())
p1.reset()
p2.rangeRK4()
plt.plot(p2.checkx(),p2.checky())
plt.show()
