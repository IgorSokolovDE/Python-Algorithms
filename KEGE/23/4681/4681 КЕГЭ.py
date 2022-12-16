def F(n):
    global x
    if n>27: return
    if n==27:
        x+=1
        return
    else:
        F(n+3)
        F(n*2)
def F2(n):
    global y
    if n>63: return
    if n==63:
        y+=1
        return
    else:
        F2(n+3)
        F2(n*2)
x=0
y=0
F(3)
F2(27)
print(x*y)
        
