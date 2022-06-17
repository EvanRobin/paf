import numpy as np
import matplotlib.pyplot as plt
import math
class P:
    def __init__(self,name,r,v,m):
        self.r  = r
        self.v  = v
        self.xs = []
        self.ys = []
        self.m=m
        self.name=name
    
    def reset(self):
        self.__init__()
    
    def checkx(self):
        return self.x 
    
    def checky(self):
        return self.y              
class S:   
    def __init__(self):
        self.planets=[]
        self.t=[0]
        self.G=6.67*10**-11
        #self.G=3
    def add_planet(self, planet):
        self.planets.append(planet)

    def evolve(self,t,time):
        while self.t[-1] < time:
            dt = t
            self.t.append(self.t[-1]+dt)
            for P in self.planets:
                a=np.array((0.,0.))
                for D in self.planets:    
                    if D!=P:
                        asuper=(self.G*D.m/((D.r[0]-P.r[0])**2+(D.r[1]-P.r[1])**2))*np.array((D.r[0]-P.r[0],D.r[1]-P.r[1]))/math.sqrt((D.r[0]-P.r[0])**2+(D.r[1]-P.r[1])**2)
                        a+=asuper
                        if D.r[0]-P.r[0]<2500 or D.r[1]-P.r[1]<2500: #not working as atended
                            break            
                P.v=P.v + a * t
                P.r=P.r + P.v * t
                P.xs.append(P.r[0])
                P.ys.append(P.r[1])
    def reverse(self,t,maxt):
        while self.t[-1] < maxt:
            dt = t
            self.t.append(self.t[-1]+dt)
            for P in self.planets:
                a=np.array((0.,0.))
                for D in self.planets:    
                    if D!=P:
                        asuper=(self.G*D.m/((D.r[0]-P.r[0])**2+(D.r[1]-P.r[1])**2))*np.array((D.r[0]-P.r[0],D.r[1]-P.r[1]))/math.sqrt((D.r[0]-P.r[0])**2+(D.r[1]-P.r[1])**2)
                        a+=asuper
                        
                P.v=(P.v + a * t)
                P.r=P.r + P.v * t
                P.xs.append(P.r[0])
                P.ys.append(P.r[1])
            