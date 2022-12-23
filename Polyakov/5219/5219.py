def F(n,kU):
    global kPr
    if n>300: return
    if n==300:
        if kU<=5:
            kPr+=1
        return
    else:
        F(n+1,kU)
        F(n*3,kU+1)
        F(n*4,kU+1)
kPr=0
F(3,0)
print(kPr)
