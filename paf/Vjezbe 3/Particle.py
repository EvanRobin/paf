import numpy as np
import matplotlib.pyplot as plt
import math
class Particle:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]
        self.ax=[]
        self.ay=[]
        self.dt=0.01
        self.angle=0       
    def set_initial_conditions(self,x0,y0,v0,angle):
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0*np.cos(angle*np.pi/180))
        self.vy.append(v0*np.sin(angle*np.pi/180))
        self.ax.append(0)
        self.ay.append(-9.81)
        self.angle=angle
    def reset(self):
        self.__init__()
    def __move(self):    
        self.t.append(self.t[-1]+self.dt)
        self.vy.append(self.vy[-1]+self.dt*self.ay[-1])
        self.vx.append(self.vx[-1]+self.dt*self.ax[-1])
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.dt*self.vy[-1])
        self.ax.append(0)
        self.ay.append(-9.81)
    def range(self):
        while self.y[-1] >= 0:
            self.__move()  
        return self.x[-1]
    def plot_trajectory(self):
        self.range()
        plt.plot(self.x,self.y)
        plt.show()
    def total_time(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.t[-1]
    def max_speed(self):
        maxspeed=0
        while self.y[-1] >= 0:
            if maxspeed<(math.sqrt(self.vx[-1]**2+self.vy[-1]**2)):
                maxspeed=(math.sqrt(self.vx[-1]**2+self.vy[-1]**2))
            self.__move()
            
                
        return maxspeed
    #def velocity_to_hit_target(self,xr,yr,r,p):#PITAJ PROFA IMAS TJEDAN
        nohit=True
        v=0.1
        self.vy.append(v*np.sin(p*np.pi/180))
        self.vx.append(v*np.cos(p*np.pi/180))
        self.__init__()
        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.angle=p
 
