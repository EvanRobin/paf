from matplotlib.animation import PillowWriter
import math
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
meteor=solar.P("metoer",np.array((-1*au,6700000.)),np.array((-24748.,-24748.)),10.0e14)
ss=solar.S()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)
ss.add_planet(meteor)
ss.evolve(day,day*96)

sun2=solar.P("sun",np.array((sun.xs[-1],sun.ys[-1])),np.array((-sun.v[0],-sun.v[1])),1.989e30)
mercury2=solar.P("mercury",np.array((mercury.xs[-1],mercury.ys[-1])),np.array((-mercury.v[0],-mercury.v[1])),3.3e24)
venus2=solar.P("venus",np.array((venus.xs[-1],venus.ys[-1])),np.array((-venus.v[0],-venus.v[1])),4.8685e24)
earth2=solar.P("earth",np.array((earth.xs[-1],earth.ys[-1])),np.array((-earth.v[0],-earth.v[1])),5.972e24)
mars2=solar.P("mars",np.array((mars.xs[-1],mars.ys[-1])),np.array((-mars.v[0],-mars.v[1])),6.417e23)
meteor2=solar.P("metoer",np.array((meteor.xs[-1],meteor.ys[-1])),np.array((-meteor.v[0],-meteor.v[1])),10.0e14)
ss.planets.remove(sun)
ss.planets.remove(mercury)
ss.planets.remove(venus)
ss.planets.remove(mars)
ss.planets.remove(meteor)
ss=solar.S()
ss.add_planet(sun2)
ss.add_planet(mercury2)
ss.add_planet(venus2)
ss.add_planet(earth2)
ss.add_planet(mars2)
ss.add_planet(meteor2)
ss.evolve(day,day*96)
fig = plt.figure()
metadata = dict(title='solarsystem2!.gif', artist='evanbrooks')
writer = PillowWriter(fps=10, metadata=metadata)
with writer.saving(fig, "solarsystem2!.gif", 100):
    for j in range(math.floor(len(earth.xs)/5)):
        i = j*5
        plt.clf()
        plt.scatter(sun2.xs[i], sun2.ys[i], color='yellow', label="sun")
        plt.plot(mercury2.xs[0:i], mercury2.ys[0:i], color="grey", label="mercury")
        plt.plot(mercury2.xs[i], mercury2.ys[i], 'o', color="grey")
        plt.plot(venus2.xs[0:i], venus2.ys[0:i], color="orange", label="venus")
        plt.plot(venus2.xs[i], venus2.ys[i], 'o', color="orange")
        plt.plot(earth2.xs[0:i], earth2.ys[0:i], color="blue", label="earth")
        plt.plot(earth2.xs[i], earth2.ys[i], 'o', color="blue")
        plt.plot(mars2.xs[0:i], mars2.ys[0:i], color="red", label="mars")
        plt.plot(mars2.xs[i], mars2.ys[i], 'o', color="red")
        plt.plot(meteor2.xs[0:i], meteor2.ys[0:i], color="red", label="meteor")
        plt.plot(meteor2.xs[i], meteor2.ys[i], 'o', color="black")
        plt.legend(loc='upper right')
        plt.xlim(-2*au, 2*au)
        plt.ylim(-2*au, 2*au)
        plt.grid()
        plt.title('Solar system with meteor')
        writer.grab_frame()
