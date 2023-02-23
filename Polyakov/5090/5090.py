def F(n):
    global x
    if (n<18)or(n==20):
        return
    if n==18:
        x+=1
        return
    else:
        F(n-1)
        F(n-2)
def F2(n):
    global y
    if (n<6)or(n==20):
        return
    if n==6:
        y+=1
        return
    else:
        F2(n-1)
        F2(n-2)
x=0
y=0
F(27)
F2(18)
print(x*y)
