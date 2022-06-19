import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import solar
au=1.496e11
day=60*60*24
year=365.242*day
sun=solar.P("sun",np.array((0.,0.)),np.array((0.,0.)),1.989e30)
earth=solar.P("earth",np.array((-1*au,0.1)),np.array((0.,29783.)),5.972e24)
ss=solar.S()
ss.add_planet(sun)
ss.add_planet(earth)
ss.evolve(day,year)
#fig=plt.figure(figsize=(10,10))
plt.scatter(sun.xs,sun.ys,label=sun.name,color="yellow",linewidth=.5)
plt.plot(earth.xs,earth.ys,label=earth.name,color="blue")
plt.show()