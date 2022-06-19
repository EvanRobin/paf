import Particle as pa
import numpy as np
import math
import matplotlib.pyplot as plt
pp=pa.Particle()
#pp.set_initial_conditions(0,0,10,60)
#pp.set_initial_conditions(0,0,7.5,60,dt=0.01)
#phi = np.linspace(0, 2*np.pi, 200)
#xpl = 1*np.cos(phi)+3
#ypl = 1*np.sin(phi)+3
#plt.plot(xpl,ypl)
#pp.plot_trajectory()
#print(pp.velocity_to_hit_target(3,3,1,60))
#print(pp.angle_to_hit_target(3,3,1,7.5))

pp.domet_vrijem_kut(10,30)
pp.domet_vrijem_fikskut(10)