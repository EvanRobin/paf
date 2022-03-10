import math
def circles(x,y,xc,yc,r):
    v=math.sqrt((x-xc)**2+(y-yc)**2)
    if r>v:
        print("Tocka je unutar kruznice")
    elif r==v:
        print("Tocka je na radijus kruznice")
    elif r<v:
        print("Tocka je izvan kruznice")

circles(1,2,3,2,2)


    


