
print("HELLO WORLD")
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
def x_y(x,y):
    l=y-x
    return l
x1=int(inputx())
y1=int(inputy())
print("Tocka",x1 ,y1 ,"Jednazba je y=x+" ,x_y(x1,y1))