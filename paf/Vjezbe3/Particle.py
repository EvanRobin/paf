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
        
        self.angle=0       
    def set_initial_conditions(self,x0,y0,v0,angle,dt=0.01):
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0*np.cos(angle*np.pi/180))
        self.vy.append(v0*np.sin(angle*np.pi/180))
        self.ax.append(0)
        self.ay.append(-9.81)
        self.angle=angle
        self.dt=dt
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
    def range_deltat(self,deltat):
        while self.t[-1]<=deltat:
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
    def xtarget(self,xt):
        while self.x[-1] <= xt:
            self.__move()
        return self.x[-1]
    def ytarget(self,xt):
        while self.x[-1] <= xt:
            self.__move()
        return self.y[-1]
    def velocity_to_hit_target(self,xt,yt,radius,angle):
        self.__init__()
        v=0
        for i in range (0,5000,1):
            v+=0.1
            self.set_initial_conditions(0,0,v,angle)
            if self.ytarget(xt) > (yt-radius) and self.ytarget(xt) < (yt+radius):
                print(v,"m/s")
                break
    def angle_to_hit_target(self,xt,yt,radius,speed):
        self.__init__()
        v=0
        for i in range (0,5000,1):
            v+=0.1
            self.set_initial_conditions(0,0,speed,v)
            if self.ytarget(xt) > (yt-radius) and self.ytarget(xt) < (yt+radius):
                print(v,"degrees")
                break
    def domet_vrijem_kut(self,vo,angle):
        self.set_initial_conditions(0,0,vo,angle)
        self.range()
        plt.plot(self.x,self.t)
        plt.show()
        self.__init__()
        self.set_initial_conditions(0,0,vo,angle)
        angles=[angle]
        while self.y[-1] >= 0:
            self.__move()
            angles.append(np.arctan(self.vy[-1]/self.vx[-1])*180/np.pi)
        plt.plot(self.t,angles)
        plt.show()  
    def domet_vrijem_fikskut(self,vo):
        angle=30
        self.set_initial_conditions(0,0,vo,angle)
        self.range()
        plt.plot(self.x,self.t)
        plt.show()
        self.__init__()
        self.set_initial_conditions(0,0,vo,angle)
        angles=[angle]
        while self.y[-1] >= 0:
            self.__move()
            angles.append(np.arctan(self.vy[-1]/self.vx[-1])*180/np.pi)
        plt.plot(self.t,angles)
        plt.show()     