import numpy as np
import matplotlib.pyplot as plt
import math
class sile:
    def __init__(self):
        
        self.t=[]
        self.x=[]
        self.vx=[]
        self.ax=[] 
        self.f=[]     
    def set_initial_conditions(self,func,m,xo,vo,dt=0.01):
        self.t.append(0)
        self.x.append(xo)
        self.vx.append(vo)
        self.f.append(func)
        self.m=m
        self.ax.append(func/self.m)
        self.dt=dt
    
        
        
    def reset(self):
        self.__init__()
    def __move(self):    
        self.t.append(self.t[-1]+self.dt)
        self.vx.append(self.vx[-1]+self.dt*self.ax[-1])
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.ax.append(self.ax+self.f[-1]/self.m)
        self.f.append(self.f(self.x,self.vx,self.t))
    def vroom(self):
        for i in range(0,100,1):
            self.__move()
        return self.f
        
    
        
        
        