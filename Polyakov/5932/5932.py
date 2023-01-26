def F(n,k1,k2,k3):
    global kPr
    if n > 25: return
    if n==25:
        if (k1>0)and(k2>0) and (k3>0):
            kPr+=1
        return
    else:
        F(n+1,k1+1,k2,k3)
        F(n+2,k1,k2+1,k3)
        F(n*2,k1,k2,k3+1)
kPr=0
F(3,0,0,0)
print(kPr)
