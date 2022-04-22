from cgitb import reset
import numpy as np
import matplotlib.pyplot as plt
import math
class ProjectileDrop:
    def __init__(self):
        self.t=[]
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]
        self.ax=[]
        self.ay=[]      
    def set_initial_conditions(self,y0,vx,dt=0.01):
        self.t.append(0)
        self.x.append(0)
        self.y.append(y0)
        self.vx.append(vx)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.dt=dt
        print("Initial conditions have been set!",self.y[0],"is the starting height and ",self.vx[0],"is the initail speed of the plane!!!")
    def set_initial_conditions_no_msg(self,y0,vx,dt=0.01):
        self.t.append(0)
        self.x.append(0)
        self.y.append(y0)
        self.vx.append(vx)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.dt=dt
    def reset(self):
        self.__init__()
    def __move(self):    
        self.t.append(self.t[-1]+self.dt)
        self.vy.append(self.vy[-1]+self.dt*self.ay[-1])
        self.vx.append(self.vx[-1]+self.dt*self.ax[-1])
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.dt*self.vy[-1])
        self.ax.append(0)
        self.ay.append(-9.81)
    def range(self):
        while self.y[-1] >= 0:
            self.__move()  
    def change_y(self,yneo):
        v=self.vx[-1]
        self.reset()
        self.set_initial_conditions_no_msg(yneo,v,dt=0.01)
        return self.vx,self.y
    def change_vx(self,vxneo):
        y=self.y[-1]
        self.reset()
        self.set_initial_conditions_no_msg(y,vxneo,dt=0.01)
        return self.vx,self.y
    def plotit(self):
        self.range()
        plt.plot(self.x,self.y)
        plt.show()
        plt.plot(self.vy,self.t)
        plt.show()
    def time(self,delt):
        while self.t[-1] >= delt:
            self.__move()
        return self.t[-1]
    def timetofall(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.t[-1]
    def DROPDABOMBMAN(self,x,r,ws):
        iny=self.y[0]
        invx=self.vx[0]+ws
        for i in range (1,100000,1):
            self.reset
            self.set_initial_conditions_no_msg(iny,invx)
            self.x=[0+i]
            self.range()
            if self.x[-1] < x+r and self.x[-1] > x-r:
                thetime=self.x[0]/self.vx[0]
                break
        return thetime
    
    def DROPDABOMBMANgraf(self,x,r,ws):
        iny=self.y[0]
        invx=self.vx[0]+ws
        for i in range (1,100000,1):
            self.reset
            self.set_initial_conditions_no_msg(iny,invx)
            self.x=[0+i]
            xj=[0+i]
            self.range()
            if self.x[-1] < x+r and self.x[-1] > x-r:
                thetime=self.x[0]/self.vx[0]
                break
        self.reset()
        self.set_initial_conditions_no_msg(iny,invx)
        self.x=xj
        self.range()
        plt.plot(self.x,self.y)
        plt.show()
             
        return thetime