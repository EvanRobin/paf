lx=np.linspace(0,1,1000)
c=ca.func(f4,0,1)
s=ca.intagral_a(f2,0,1)
plt.plot(lx,c)
plt.plot(lx,s)
plt.show()
for i in lx:
    f+=1
for i in c:
    f+=1
for i in s:
    f+=1
print(f)
def func(f,a,b):
    inta=[]
    c=0
    lx=np.linspace(a,b,1000)
    for i in range (0,999,1):
        c+=module.value(f,lx[i])
        inta.append(c)
    return inta
    for i in range(0,10,1):
    
    fu.append(ca.intagral_a(f2,f,fo))
    
plt.plot(np.repeat(module.value(f4,1)),np.linspace(0,1000,10))
plt.plot(fu,np.linspace(0,1000,10),'r')
plt.show()
