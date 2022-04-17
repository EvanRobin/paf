import matplotlib.pyplot as plt
import numpy as np
import math
class Force:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.F = []   
    def set_in_conditions(self, x0, v0, m, s, intt, dt=0.01):
        self.m = m
        self.dt = dt
        self.intt = intt
        self.sila = s
        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(s(x0, v0, self.dt)/self.m)
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a.append(self.sila(self.x[-1], self.v[-1], self.t[-1])/self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)
    def gibanje(self):
        while self.t[-1] < self.intt:
            self.__move()
        return self.t, self.x, self.v, self.a