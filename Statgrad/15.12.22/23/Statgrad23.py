def F(n,kom,kol1,kol2):
    global kPr
    if n>14:
        return
    if n==14:
        kPr+=1
    if kom==0:
        F(n+1,1,1,0)
        F(n*2,2,0,1)
    else:
        if kom==1:
            if kol1<2:
                F(n+1,1,kol1+1,0)
                F(n*2,2,0,1)
            else:
                F(n*2,2,0,1)
        else:
            if kol2<2:
                F(n+1,1,1,0)
                F(n*2,2,0,kol2+1)
            else:
                F(n*2,2,0,1)
                F(n+1,1,1,0)
kPr=0
F(1,0,0,0)
print(kPr)
