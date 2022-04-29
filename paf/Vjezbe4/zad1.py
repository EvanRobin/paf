import calcules as ca
import math
import numpy as np
import matplotlib.pyplot as plt
import module
def f2(x):
    return math.sin(x)
def f1(x):
    return x
def f3(x):
    return (1/2)*(x**2)
def f4(x):
    return 1*math.cos(x)
koraci=0
lisp=[]
lisp2=[]
tr=[]
for i in range(0,10,1):
    koraci+=100
    il,iu=ca.intagral_a(f1,0,1,koraci)
    lisp.append(il)
    lisp2.append(iu)
    tr.append(ca.intagral_b(f1,0,1,koraci))
plt.scatter(np.linspace(0,1000,10),lisp)
plt.scatter(np.linspace(0,1000,10),lisp2)
plt.scatter(np.linspace(0,1000,10),tr)
plt.plot(np.linspace(0,1000,10),np.repeat(module.value(f3,1),10))
plt.show()
print(tr)
print(lisp2)