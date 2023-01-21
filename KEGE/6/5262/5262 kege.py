import turtle as t
t.speed(0)
x=0
y=0
for i in range(20):
    t.circle(4)
    x=x+8
    t.goto(x,y)
y=y-12
t.goto(x,y)
for i in range(10):
    t.circle(8)
    x=x-16
    t.goto(x,y)
y=y-14
t.goto(x,y)
for i in range(15):
    t.circle(6)
    x=x+12
    t.goto(x,y)
    
