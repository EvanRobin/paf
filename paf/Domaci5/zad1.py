import numpy as np
import math
import magneticfield as m
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = plt.axes(projection = '3d')
p1=m.E()
p2=m.E()
#m=9.11*(10**(-31))
m=1.0
def promj(t):
    bx = 0.0
    by = 0.0
    bz = 0.1*t
    return np.array((bx, by, bz))
p1.set_initial_conditions(0.0,0.0,0.0,m)
p1.set_initial_conditions_DELUXEEDITION((0.0,0.0,0.0),(0.0,0.0,1.0),(0.1,0.1,0.1),1.0)
p1.journey(10.0)
ax.plot3D(p1.x,p1.y,p1.z)
p2.set_initial_conditions(0.0,0.0,0.0,m)
p2.set_initial_conditions_DELUXEEDITION((0.0,0.0,0.0),promj,(0.1,0.1,0.1),1.0)
p2.journeyBtFUNCTION(10.0)
ax.plot3D(p2.x,p2.y,p2.z)
plt.show()