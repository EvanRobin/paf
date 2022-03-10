def inputx():
    x=(input("Unesi x: "))
    if x.isdigit:
        print("Hvala na inputu")
    else:
        x=(input("Unesi x koji je broj"))
    return x
def inputy():
    y=(input("Unesi y: "))
    if y.isdigit:
        print("Hvala na inputu")
    else:
        y=(input("Unesi y koji je broj"))
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