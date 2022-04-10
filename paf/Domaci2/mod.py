import numpy as np
import matplotlib.pyplot as plt
class F():
    def __init__(self):
        self.m = []
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.force = []      
    def reset(self):
        self.__init__()      
    def set_initial_conditions(self, F, m, v0, x0,dt=0.01):
        self.m.append(m)
        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.dt=dt
        self.force.append(F(self.v[-1], self.x[-1], self.t[-1]))
        self.a.append(F(self.v[-1], self.x[-1], self.t[-1])/self.m[-1])      
    
        
    