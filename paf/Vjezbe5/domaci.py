import numpy as np
import math
import matplotlib.pyplot as plt
import SILE as si                                         



import module
import math
import numpy as np
import matplotlib.pyplot as plt
def value(func,x):
    return(func(x))   
def f(x,v,t):
    return 10
#def derive_dot2(f,x):
    #return (module.value(f,x)-module.value(f,x-dx))/dx
#def derive_dot3(f,x):
    #return (module.value(f,x+dx)-module.value(f,x-dx))/2*dx

x=0
v=0
t=0
def f(x,v,t):
    return float(10)
s=si.sile()
s.set_initial_conditions(f(x,v,t),1,0,0)
print(s.vroom())