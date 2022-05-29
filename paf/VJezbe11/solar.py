import numpy as np
import matplotlib.pyplot as plt
import math
class P:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.y=[]
        self.v=np.array((0.0,0.0))
        self.a=np.array((0.0,0.0))
        self.m=0.0
        self.G=6.67*10**-11

    def set_initial_conditions(self,xo,yo,m,dt=0.01):
        self.t.append(0)
        self.x.append(xo)
        self.y.append(yo)
        self.m=m
        self.dt=dt
    
    def reset(self):
        self.__init__()

    def checkx(self):
        return self.x 
    def checky(self):
        return self.y          
        
class S:
    def __move(self):
        