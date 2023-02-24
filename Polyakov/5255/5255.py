def F(n,kCh):
    global kPr
    if n>402:
        return
    if n==402:
        if kCh<=3:
            kPr+=1
        return
    else:
        if (n+2)%2==0:
            F(n+2,kCh+1)
        else:
            F(n+2,kCh)
        F(n*2,kCh+1)
        if (n*3)%2==0:
            F(n*3,kCh+1)
        else:
            F(n*3,kCh)
kPr=0
F(1,0)
print(kPr)
