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
          
    def journey(self,t):
        while self.t[-1] < t:
            self.__move()
    def journeyBt(self,t,b):
        while self.t[-1] < t:
            self.t.append( self.t[-1] + self.dt )
            self.a = (self.E+np.cross(self.v,self.B))*self.q/self.m
            self.B = self.B + np.array((0.0,0.0,b))
            #print(self.B)
        
            self.v += self.a*self.dt
        
            self.x.append( self.x[-1] + self.v[0]*self.dt )
            self.y.append( self.y[-1] + self.v[1]*self.dt )
            self.z.append( self.z[-1] + self.v[2]*self.dt )  
          
    def checkx(self):
        return self.x 
    def checky(self):
        return self.y 
    def checkz(self):
        return self.z 
    
    def __af(self, v):
        return self.q/self.m * (self.E + np.cross(v, self.B(self.t[-1])))
         
    def journeyBtFUNCTION(self,t):
        while self.t[-1] < t:
            self.t.append( self.t[-1] + self.dt )
            self.a = self.__af(self.v)
            #print(self.B)
        
            self.v += self.a*self.dt
        
            self.x.append( self.x[-1] + self.v[0]*self.dt )
            self.y.append( self.y[-1] + self.v[1]*self.dt )
            self.z.append( self.z[-1] + self.v[2]*self.dt ) 
        