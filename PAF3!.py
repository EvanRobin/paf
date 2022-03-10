import numpy as np
from matplotlib import pyplot as plt
def so_much_fun(x,y,x1,y1):
    m=(y1-y)/(x1-x)
    l=-m*x+y
    print("Kroz tocke",x1,y1,"i",x,y,"Prolazi ppravac y=",m,"x+",l)
    plt.plot(x, f(x), color='red')
so_much_fun(1,1,2,2)
