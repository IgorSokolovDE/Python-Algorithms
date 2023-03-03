import turtle as t
t.left(90)
for k in range(5):
    for i in range(4):
        t.forward(30*3)
        t.right(90)
    t.color("red")
    t.forward(5*3)
    t.right(90)
    t.forward(5*3)
    t.color("black")
    t.right(270)
