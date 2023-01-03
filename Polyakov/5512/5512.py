import turtle as t
x=0
y=0
for i in range(7):
    x+=6; y-=9
    t.goto(x,y)
    x-=6; y+=2
    t.goto(x,y)
    x+=12; y+=3
    t.goto(x,y)
