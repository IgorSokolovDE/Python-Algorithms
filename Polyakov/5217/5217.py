def F(n,kUm):
    global kPr
    if n>100: return
    if n==100:
        if kUm<=2:
            kPr+=1
        return
    else:
        F(n+1,kUm)
        F(n*2,kUm+1)
        F(n*3,kUm+1)
kPr=0
F(1,0)
print(kPr)
