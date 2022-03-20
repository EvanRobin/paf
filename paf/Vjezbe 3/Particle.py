import numpy as np
class Particle:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]
        self.ax=[]
        self.ay=[]
        self.dt=0.01
        
    def set_initial_conditions(self,x0,y0,v0,angle):
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0*np.cos(angle))
        self.vy.append(v0*np.sin(angle))
        self.ax.append(0)
        self.ay.append(-9.81)
        

    def reset(self):
        self.__init__()

    def __move(self):
        
        self.t.append(self.t[-1]+self.dt)
        self.vy.append(self.vy[-1]+self.dt*self.ay[-1])
        self.vx.append(self.vx[-1]+self.dt*self.ax[-1])
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.dt*self.ay[-1])
        self.ax.append(0)
        self.ay.append(-9.81)
        

    def range(self):
        while self.y[-1] >= 0:
            self.__move()
        
        return self.x[-1]
            


    

    