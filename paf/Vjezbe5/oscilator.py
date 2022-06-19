import matplotlib.pyplot as plt
import numpy as np
import math

class HO:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        
    def set_initial_conditions(self, x0, m, k, dt):
        self.t.append(0)
        self.x.append(x0)
        self.v.append(0)
        self.a.append((-k/m)*x0)
        self.A = x0
        self.m = m
        self.k = k
        self.dt = dt
        self.periodo = 2*np.pi/np.sqrt(k/m)
    def reset(self):
        self.__init__()
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a.append((-self.k/self.m)*self.x[-1])
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)

    def journey(self,t):
        while self.t[-1] < t:
            self.__move()
        return self.t, self.x, self.v, self.a

    def analitical(self):
        t = np.linspace(0, 10, 10000)
        for i in t:
            self.x.append(self.A*math.cos(math.sqrt(self.k/self.m)*i))
            self.v.append(-self.A*math.sqrt(self.k/self.m)*math.sin(math.sqrt(self.k/self.m)*i))
            self.a.append(-self.A*(self.k/self.m)*math.cos(math.sqrt(self.k/self.m)*i))
        del self.x[-1], self.v[-1], self.a[-1]
        return t, self.x, self.v, self.a

    def period(self):
        while self.v[-1] <= 0:
            self.__move()
        while self.v[-1] > 0:
            self.__move()
        return(self.t[-1],self.periodo)