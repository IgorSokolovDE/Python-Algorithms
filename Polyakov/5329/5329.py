def f(n):
    global x
    if n<12: return
    if n==12:
        x+=1
        return
    else:
        f(n-1)
        f(n//2)
def f2(n):
    global y
    if n<1: return
    if n==1:
        y+=1
        return
    else:
        f2(n-1)
        f2(n//2)
x=0
y=0
f(30)
f2(12)
print(x*y)
