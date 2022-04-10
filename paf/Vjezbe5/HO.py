import numpy as np
import matplotlib.pyplot as plt
import math
class HO:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.vx=[]
        self.ax=[]      
    def set_initial_conditions(self,x0,vx,k,m,dt=0.01):
        self.t.append(0)
        self.x.append(x0)
        self.vx.append(vx)
        self.ax.append(-(k*x0/m))
        self.dt=dt
        self.k=k
        self.m=m
    def reset(self):
        self.__init__()
    def __move(self):    
        self.t.append(self.t[-1]+self.dt)
        self.vx.append(self.vx[-1]+self.dt*self.ax[-1])
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.ax.append(-(self.k*self.x[-1]/self.m))
    def swings(self,tics):
        for i in range(0,tics,1):
            self.__move()
    def plot_xt_vxt_axt(self,deltat):
        tics=int(deltat/self.dt)
        self.swings(tics)
        plt.plot(self.t,self.x)
        plt.show()
        plt.plot(self.t,self.vx)
        plt.show()
        plt.plot(self.t,self.ax)
        plt.show()
    def period(self):
        x=self.x[-1]
        t=0
        self.t=[0]
        while t<3:
            self.__move()
            if x>=self.x[-1] and x<=self.x[-2]:
                t+=1
            elif x<=self.x[-1] and x>=self.x[-2]:
                t+=1
        #plt.plot(self.t,self.x)
        #plt.show()
        return self.t[-1]
    def plot_xt(self,deltat):
        tics=int(deltat/self.dt)
        self.swings(tics)
        plt.scatter(self.t[::10],self.x[::10])
    def plot_xtp(self,deltat):
        tics=int(deltat/self.dt)
        self.swings(tics)
        plt.scatter(self.t[::3],self.x[::3],s=3)
    def ana(self,xo,deltat,k,m):
        self.set_initial_conditions(xo,0,k,m)
        tics=int(deltat/self.dt)
        sinus=[0]
        self.t=[0]
        for i in range(0,tics,1):
            self.t.append(self.t[-1]+self.dt)
            sinus.append(xo*np.sin(math.sqrt(self.k/self.m)*self.t[-1]+np.pi/2))
        plt.plot(self.t,sinus,'r')
                        
        
    
        