def F(n,E):
    global kPr
    if (n>5500)or(E<0): return
    if n==5500:
        if E==0:
           kPr+=1
        return
    else:
        F(n+3,E-len(str(n)))
        F(n*4,E-len(str(n)))
        F(n*5,E-len(str(n)))
kPr=0
F(1,1000)
print(kPr)
        
