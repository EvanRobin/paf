
def inputx():    
    while True:
        a=(input("Unesi unesi integer x: "))
        if a.isdigit():
            break
        print("unos treba bit integer")
    return a
def inputy():       
    while True:
        a=(input("Unesi unesi integer y: "))
        if a.isdigit():
            break
        print("unos treba bit integer")
    return a
x1=int(inputx())
y1=int(inputy())
x2=int(inputx())
y2=int(inputy())
def tupa(x,y,xo,yo):
    m=(yo-y)/(xo-x)
    return m

l=-tupa(x1,y1,x2,y2)*x1+y1

print("Kroz tocke",x1,y1,"i",x2,y2,"Prolazi ppravac y=",tupa(x1,y1,x2,y2),"x+",l)
