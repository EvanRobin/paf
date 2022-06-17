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
meteor=solar.P("metoer",np.array((1.2*au,.6*au)),np.array((-1750.,0.)),10.0e14)
ss=solar.S()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)
ss.add_planet(meteor)
ss.evolve(day,day*95)
#fig=plt.figure(figsize=(10,10))
fig = plt.figure()
metadata = dict(title='solarsystem2!.gif', artist='evanbrooks')
writer = PillowWriter(fps=10, metadata=metadata)
with writer.saving(fig, "solarsystem2!.gif", 100):
    for j in range(math.floor(len(earth.xs)/5)):
        i = j*5
        plt.clf()
        plt.scatter(sun.xs[i], sun.ys[i], color='yellow', label="sun")
        plt.plot(mercury.xs[0:i], mercury.ys[0:i], color="grey", label="mercury")
        plt.plot(mercury.xs[i], mercury.ys[i], 'o', color="grey")
        plt.plot(venus.xs[0:i], venus.ys[0:i], color="orange", label="venus")
        plt.plot(venus.xs[i], venus.ys[i], 'o', color="orange")
        plt.plot(earth.xs[0:i], earth.ys[0:i], color="blue", label="earth")
        plt.plot(earth.xs[i], earth.ys[i], 'o', color="blue")
        plt.plot(mars.xs[0:i], mars.ys[0:i], color="red", label="mars")
        plt.plot(mars.xs[i], mars.ys[i], 'o', color="red")
        plt.plot(meteor.xs[0:i], meteor.ys[0:i], color="red", label="meteor")
        plt.plot(meteor.xs[i], meteor.ys[i], 'o', color="black")
        plt.legend(loc='upper right')
        plt.xlim(-2*au, 2*au)
        plt.ylim(-2*au, 2*au)
        plt.grid()
        plt.title('Solar system with meteor')
        writer.grab_frame()
