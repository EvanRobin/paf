import matplotlib.pyplot as plt
def inputx():
    x=int(input("Unesi x: "))
    return x
def inputy():
    y=int(input("Unesi y: "))
    return y
x1=int(inputx())
y1=int(inputy())
x2=int(inputx())
y2=int(inputy())
def tupa(x,y,xo,yo):
    m=(yo-y)/(xo-x)
    return m

l=-tupa(x1,y1,x2,y2)*x1+y1

print("Kroz tocke",x1,y1,"i",x2,y2,"Prolazi ppravac y=",tupa(x1,y1,x2,y2),"x+",l)
plt.plot([x1,x2],[y1,y2])
