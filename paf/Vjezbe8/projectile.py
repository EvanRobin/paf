import numpy as np
import matplotlib.pyplot as plt
import math
class Fric:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.vx=[]
        self.ax=[] 
        self.y=[]
        self.vy=[]
        self.ay=[]
        self.fx=[] 
        self.fy=[] 
        self.angle=0
        self.cd=0
        self.m=0
        self.A=0
        self.g=0
        self.p=0
    def set_initial_conditions(self,xo,yo,alpha,vo,cd,A,p,m,dt=0.01):
        self.t.append(0)
        self.x.append(xo)
        self.y.append(yo)
        self.angle=(alpha)
        self.vx.append(vo*np.cos((alpha/180)*np.pi))
        self.vy.append(vo*np.sin((alpha/180)*np.pi))
        self.g=-9.81
        self.dt=dt
        self.ax.append(0)  
        self.ay.append(0)
        self.cd=(cd)
        self.A=(A)
        self.p=(p)
        self.m=m
    #def friction_conditions(self,cd,A,p,m):
        #self.cd=(cd)
        #self.A=(A)
        #self.p=(p)
        #self.m=m
    def reset(self):
        self.__init__()
    def __ax(self, v):
        return -np.sign(v)*(self.p*self.cd*self.A)/(2*self.m)*(v)**2
    def __ay(self, v):
        return self.g-np.sign(v)*(self.p*self.cd*self.A)/(2*self.m)*(v)**2
    #def __move(self):    
        #self.t.append(self.t[-1]+self.dt)
        #self.ax.append(self.__ax(self.vx[-1]))
        #self.ay.append(self.__ay(self.vy[-1]))
        #self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        #self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        #self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        #self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def __move(self,dt):    
        self.t.append(self.t[-1]+dt)
        self.ax.append(self.__ax(self.vx[-1]))
        self.ay.append(self.__ay(self.vy[-1]))
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
    def range(self,dt):
         while self.y[-1] >= 0:
                self.__move(dt)
    def cred(self,dt):
        while self.y[-1] >= 0:
                self.__move(dt)
        if self.y[-1] < -0.01:
            credibility="dt isn't viable"
        else:
            credibility="dt is viable"
        return credibility
    def __moveRK4(self,dt=0.01):
        k1x=self.vx[-1]*dt
        k1y=self.vy[-1]*dt
        k1vx=self.__ax(self.vx[-1])*dt
        k1vy=self.__ay(self.vy[-1])*dt
        k2x = (self.vx[-1]+k1vx/2)*dt
        k2y = (self.vy[-1]+k1vy/2)*dt
        k2vx = self.__ax(self.vx[-1]+k1vx/2)*dt
        k2vy = self.__ay(self.vy[-1]+k1vy/2)*dt
        k3x = (self.vx[-1]+k2vx/2)*dt
        k3y = (self.vy[-1]+k2vy/2)*dt
        k3vx = self.__ax(self.vx[-1]+k2vx/2)*dt
        k3vy = self.__ay(self.vy[-1]+k2vy/2)*dt
        k4x = (self.vx[-1]+k3vx)*dt
        k4y = (self.vy[-1]+k3vy)*dt
        k4vx = self.__ax(self.vx[-1]+k3vx)*dt
        k4vy = self.__ay(self.x[-1]+k3vy)*dt
        self.vx.append(self.vx[-1]+(k1vx+2*k2vx+2*k3vx+k4vx)/6)
        self.vy.append(self.vy[-1]+(k1vy+2*k2vy+2*k3vy+k4vy)/6)
        self.x.append(self.x[-1]+(k1x+2*k2x+2*k3x+k4x)/6)
        self.y.append(self.y[-1]+(k1y+2*k2y+2*k3y+k4y)/6)
        self.t.append(self.t[-1]+dt)        
    def rangeRK4(self,dt=0.01):
        while self.y[-1] >= 0:
            self.__moveRK4(dt)
    def rangeRK4deluxe(self,dt=0.01):
        while self.y[-1] >= 0:
            self.__moveRK4(dt)
        return self.x[-1]
    def checkt(self):
        return self.t
    def checkx(self):
        return self.x
    def checkvx(self):
        return self.vx
    def checkax(self):
        return self.ax    
    def checky(self):
        return self.y
    def checkvy(self):
        return self.vy
    def checkay(self):
        return self.ay
    def checkm(self):
        return self.m
    def dom(self):
        return self.x[-1]
    def cd(self):
        return self.cd
    
        
    
        
        
        