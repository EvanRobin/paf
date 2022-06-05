import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import solar
au=1.496e11
day=60*60*24
year=365.242*day
sun=solar.P("sun",np.array((0.,0.)),np.array((0.,0.)),1.989e30)
mercury=solar.P("mercury",np.array((0.2,0.466*au)),np.array((-47362.,0.0)),3.3e24)
venus=solar.P("venus",np.array((0.723*au,0.3)),np.array((0.,35020.)),4.8685e24)
earth=solar.P("earth",np.array((-1*au,0.1)),np.array((0.,29783.)),5.972e24)
mars=solar.P("mars",np.array((0.4,-1.666*au)),np.array((24007.,0.)),6.417e23)

ss=solar.S()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)

ss.evolve(day,year*10)
#fig=plt.figure(figsize=(10,10))
plt.plot(sun.xs,sun.ys,label=sun.name,color="yellow",linewidth=5.0)
plt.plot(earth.xs,earth.ys,label=earth.name,color="blue")
plt.plot(mercury.xs,mercury.ys,label=mercury.name,color="brown")
plt.plot(venus.xs,venus.ys,label=venus.name,color="orange")
plt.plot(mars.xs,mars.ys,label=mars.name,color="red")


plt.show()