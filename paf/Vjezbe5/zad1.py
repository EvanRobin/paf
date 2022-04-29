import numpy as np
import math
import matplotlib.pyplot as plt
import HO as ho                                          
h1=ho.HO()
#h1.set_initial_conditions(3,0,2,1)
#h1.plot_xt_vxt_axt(10)
#print(h1.period())
deltat=10
h1.set_initial_conditions(3,0,2,1,0.05)
h1.plot_xt(deltat)

h1.set_initial_conditions(3,0,2,1,0.01)
h1.plot_xtp(deltat)

h1.ana(3,deltat,2,1)
plt.show()

