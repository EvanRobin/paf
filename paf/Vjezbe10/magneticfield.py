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
        
    def set_initial_conditions_DELUXEEDITION(self,E,B,q):
        self.E=E
        self.B=B
        self.q=q
    def set_velocity(self, x_coordinate, y_coordinate, z_coordinate):
        self.v = np.array([x_coordinate, y_coordinate, z_coordinate])    
    
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
    '''
    def __moveRK4(self):
        self.t.append( self.t[-1] + self.dt )
        k1v=(self.E+np.cross(self.v,self.B))*self.q/self.m*self.dt
        k1x=self.v[0]*self.dt
        k1y=self.v[1]*self.dt
        k1z=self.v[2]*self.dt
        k2v=(self.E+np.cross(k1v/2,self.B))*self.q/self.m*self.dt*self.dt
        k2x=(self.v[0]+k1v)*self.dt
        k2y=(self.v[1]+k1v)*self.dt
        k2z=(self.v[2]+k1v)*self.dt
        k3v=(self.E+np.cross(k2v/2,self.B))*self.q/self.m*self.dt*self.dt
        k3x=(self.v[0]+k2v)*self.dt
        k3y=(self.v[1]+k2v)*self.dt
        k3z=(self.v[2]+k2v)*self.dt
        k4v=(self.E+np.cross(k3v/2,self.B))*self.q/self.m*self.dt*self.dt
        k4x=(self.v[0]+k3v)*self.dt
        k4y=(self.v[1]+k3v)*self.dt
        k4z=(self.v[2]+k3v)*self.dt
        self.v+=(k1v+2*k2v+2*k3v+k4v)/6
        self.x.append(self.x[-1]+(k1x+2*k2x+2*k3x+k4x)/6)
        self.y.append(self.y[-1]+(k1y+2*k2y+2*k3y+k4y)/6)
        self.z.append(self.z[-1]+(k1z+2*k2z+2*k3z+k4z)/6)
    '''#ovaj izbacuje manje errora
    def __moveRK4(self):
        self.t.append( self.t[-1] + self.dt )
        k1v = self.ace(self.v)*self.dt
        k1r = self.v*self.dt
        k2v = self.ace(self.v+k1v/2)*self.dt
        k2r = (self.v+k1v/2)*self.dt
        k3v = self.ace(self.v+k2v/2)*self.dt
        k3r = (self.v+k2v/2)*self.dt
        k4v = self.ace(self.v+k3v)*self.dt
        k4r = (self.v+k3v)*self.dt
        self.v += (k1v+2*k2v+2*k3v+k4v)/6
        self.x.append(self.x[-1]+(k1r[0]+2*k2r[0]+2*k3r[0]+k4r[0])/6)
        self.y.append(self.y[-1]+(k1r[1]+2*k2r[1]+2*k3r[1]+k4r[1])/6)
        self.z.append(self.z[-1]+(k1r[2]+2*k2r[2]+2*k3r[2]+k4r[2])/6)
    def ace(self,v):
        return (self.E+np.cross(v,self.B))*self.q/self.m
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