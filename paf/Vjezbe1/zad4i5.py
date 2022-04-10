import matplotlib.pyplot as plt
import numpy as np
def so_much_fun(x,y,x1,y1):   
    xa=[x,x1]
    ya=[y,y1]
    m=(y1-y)/(x1-x)
    l=-m*x+y
    print("Kroz tocke",x1,y1,"i",x,y,"Prolazi ppravac y=",m,"x+",l)
    plt.plot(xa,ya)
    plt.plot(x, y, "s")
    plt.plot(x1, y1, "s")
    pd=input("Napisi 1 ako hoces da se spremi kao pdf: ")
    if pd=="1":
        plt.savefig("graph.png",bbox_inches="tight",pad_inches=2)
    else:
        plt.show()


so_much_fun(1,1,2,2)