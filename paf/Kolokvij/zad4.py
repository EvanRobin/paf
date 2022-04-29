import ProjectileDrop as pa
import numpy as np
import math
import matplotlib.pyplot as plt
p5=pa.ProjectileDrop()
vx=200
y=2000
#delt=8
p5.set_initial_conditions(y,vx)
deltas=np.linspace(0.001,0.1,100)
hundred=np.linspace(1,100,100)
times=[]
for i in deltas:
    p5.set_initial_conditions_no_msg(y,vx,i)
    times.append(p5.timetofall())
plt.plot(hundred,times)
plt.show()    