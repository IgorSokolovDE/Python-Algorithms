def F(n):
    global k1
    if n>16: return
    if n==16:
        k1+=1
        return
    else:
        F(n+3)
        F(n*4)
        F(n*5)
def F2(n,kA):
    global k2
    if (n>140)or(kA >4):
        return
    if n==140:
        if kA<=4:
           k2+=1
        return
    else:
        F2(n+3,kA+1)
        F2(n*4,kA)
        F2(n*5,kA)
def F3(n):
    global k3
    if n>725: return
    if n==725:
        k3+=1
        return
    else:
        F3(n+3)
        F3(n*4)
        F3(n*5)
k1=k2=k3=0
F(1)
F2(16,0)
F3(140)
print(k1*k2*k3)
        
        
