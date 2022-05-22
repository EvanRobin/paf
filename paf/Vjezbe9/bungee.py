import numpy as np
import matplotlib.pyplot as plt
import math
class Bung:
    def __init__(self):
        self.t=[] 
        self.y=[]
        self.vy=[]
        self.ay=[]
        self.fy=[] 
        self.cd=0
        self.m=0
        self.A=0
        self.g=0
        self.p=0
        self.Eel=[]
        self.Eki=[]
        self.Eg=[]
        self.EUK=[]
    def set_initial_conditions(self,yo,vo,cd,A,p,m,l,dt=0.01):
        self.t.append(0)
        self.y.append(yo)        
        self.vy.append(vo)
        self.g=-9.81
        self.dt=dt 
        self.ay.append(0)
        self.cd=(cd)
        self.A=(A)
        self.p=(p)
        self.m=m
        self.l=l
        self.Eel.append((-1)*(1/2)*self.l*self.y[-1])
        self.Eg.append((-1)*self.g*self.y[-1]*self.m)
        self.Eki.append((0.5)*self.vy[-1]**2*self.m)
        self.EUK.append((-1)*(1/2)*self.l*self.y[-1]+(-1)*self.g*self.y[-1]*self.m+(1/2)*self.vy[-1]**2*self.m)
    def reset(self):
        self.__init__()
    def __ay(self, v):
        return self.g-np.sign(v)*(self.p*self.cd*self.A)/(2*self.m)*(v)**2+(-1)*self.y[-1]*self.l
    def __ay2(self, v):
        return self.g+(-1)*self.y[-1]*self.l


    def __move(self):    
        self.t.append(self.t[-1]+self.dt)
        self.ay.append(self.__ay(self.vy[-1]))
        self.Eel.append((-1)*(1/2)*self.l*self.y[-1])
        self.Eg.append(-1*self.g*self.y[-1]*self.m)
        self.Eki.append((0.5)*self.vy[-1]**2*self.m)
        self.EUK.append((-1)*(1/2)*self.l*self.y[-1]+(-1)*self.g*self.y[-1]*self.m+(1/2)*self.vy[-1]**2*self.m)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        
    def __move2(self):    
        self.t.append(self.t[-1]+self.dt)
        self.ay.append(self.__ay2(self.vy[-1]))
        self.Eel.append((-1)*(1/2)*self.l*self.y[-1])
        self.Eg.append(-1*self.g*self.y[-1]*self.m)
        self.Eki.append((0.5)*(self.vy[-1]**2)*self.m)
        self.EUK.append((-1)*(1/2)*self.l*self.y[-1]+(-1)*self.g*self.y[-1]*self.m+(1/2)*self.vy[-1]**2*self.m)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def weee(self,time):
         while self.t[-1] <= time:
            self.__move()
    def weee_NO_FRICTION(self,time):
         while self.t[-1] <= time:
            self.__move2()
    def checkt(self):
        return self.t  
    def checky(self):
        return self.y
    def checkvy(self):
        return self.vy
    def checkay(self):
        return self.ay
    def checkm(self):
        return self.m
    def cd(self):
        return self.cd
    def checkEel(self):
        return self.Eel
    def checkEg(self):
        return self.Eg
    def checkEki(self):
        return self.Eki
    def checkEUK(self):
        return self.EUK
    
    

