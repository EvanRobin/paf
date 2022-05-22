import numpy as np
import matplotlib.pyplot as plt
import math
#ax = plt.axes(projection = '3d')
class E:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.y=[]
        self.z=[]
        self.E=np.array((0.0,0.0,0.0))
        self.B=np.array((0.0,0.0,0.0))
        self.v=np.array((0.0,0.0,0.0))
        self.a=np.array((0.0,0.0,0.0))
        self.m=0.0
        self.q=0.0

    def set_initial_conditions(self,xo,yo,zo,m,dt=0.01):
        self.t.append(0)
        self.x.append(xo)
        self.y.append(yo)
        self.z.append(zo)
        self.m=m
        self.dt=dt
        
    def set_initial_conditions_DELUXEEDITION(self,E,B,v,q):
        self.E=E
        self.B=B
        self.v=v
        self.q=q
        
    
    def reset(self):
        self.__init__()
    
    def __move(self):
        #a=(E+vxB)q/m
        self.t.append( self.t[-1] + self.dt )
        self.a = (self.E+np.cross(self.v,self.B))*self.q/self.m
        #print(self.a,"a")
        #print(self.v,"v")
        
        self.v += self.a*self.dt
        #print(self.v,"v2")
        self.x.append( self.x[-1] + self.v[0]*self.dt )
        self.y.append( self.y[-1] + self.v[1]*self.dt )
        self.z.append( self.z[-1] + self.v[2]*self.dt )
    def __moveRK4(self):
        self.t.append( self.t[-1] + self.dt )
        self.a = (self.E+np.cross(self.v,self.B))*self.q/self.m
        k1v=((self.E+np.cross(self.v,self.B))*self.q/self.m)*self.dt
        k1x=self.v[0]*self.dt
        k1y=self.v[1]*self.dt
        k1z=self.v[2]*self.dt
        k2v=((self.E+np.cross(k1v/2,self.B))*self.q/self.m)*self.dt
        k2x=(self.v[0]+k1v[0])*self.dt
        k2y=(self.v[1]+k1v[1])*self.dt
        k2z=(self.v[2]+k1v[2])*self.dt
        k3v=((self.E+np.cross(k2v/2,self.B))*self.q/self.m)*self.dt
        k3x=(self.v[0]+k2v[0])*self.dt
        k3y=(self.v[1]+k2v[1])*self.dt
        k3z=(self.v[2]+k2v[2])*self.dt
        k4v=((self.E+np.cross(k3v/2,self.B))*self.q/self.m)*self.dt
        k4x=(self.v[0]+k3v[0])*self.dt
        k4y=(self.v[1]+k3v[1])*self.dt
        k4z=(self.v[2]+k3v[2])*self.dt
        self.v = ((self.E+np.cross((k1v+2*k2v+2*k3v+k4v)/6,self.B))*self.q/self.m)*self.dt

    def journey(self,t):
        while self.t[-1] < t:
            self.__move()
    
    def journeyRK4(self,t):
        while self.t[-1] < t:
            self.__moveRK4()
    def checkx(self):
        return self.x 
    def checky(self):
        return self.y 
    def checkz(self):
        return self.z          
        
        