#Napišite svoj modul "kinematika.py" koji će sadržavati funkcije jednoliko_gibanje() i kosi_hitac(). Neka
#funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, iznos brzine, kut
#otklona, masa, vrijeme, ...) i neka crtaju iste grafove kao i u prošlim zadatcima. Napravite novi program u
#kojem ćete uključiti razvijeni modul i pozvati obe funkcije.
import numpy as np
import matplotlib.pyplot as plt
def jednoliko_gibanje(f,v,a,m,t):
    lvx=[]
    lvy=[]
    lx=[0]
    ly=[0]
    la=f/m
    dt=t/101
    lvx=v*np.cos(a*np.pi/180)
    lvy=v*np.sin(a*np.pi/180)
    lt=np.linspace(0,t,101)
    for i in range(0,100,1):
        lx.append(lx[-1]+dt*lvx)
        ly.append(ly[-1]+dt*lvy)
    
    plt.plot(lx, ly)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.show()
    
    plt.plot(lt, lx)
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.show()
    
    plt.plot(lt, ly)
    plt.xlabel("t(s)")
    plt.ylabel("y(m)")

    plt.show()
def kosi_hitac(f,v,a,m,t):
    lvy=[v*np.sin(a*np.pi/180)]
    lx=[0]
    ly=[0]
    la=f/m
    dt=t/101
    lvx=v*np.cos(a*np.pi/180)
    lt=np.linspace(0,t,101)
    for i in range(0,100,1):
        lvy.append(lvy[-1]+dt*la)
        lx.append(lx[-1]+dt*lvx)
        ly.append(ly[-1]+dt*lvy[-1])
    plt.plot(lx, ly)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.show()
    
    plt.plot(lt, lx)
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.show()
    
    plt.plot(lt, ly)
    plt.xlabel("t(s)")
    plt.ylabel("y(m)")

    plt.show()
