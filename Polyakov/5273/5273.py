def F(n,k1,k2,k3):
    global kPr
    if n>2970:
        return
    if n==2970:
        if (k1<=4)and(k2>=2)and(k3==5):
            kPr+=1
        return
    else:
        F(n*5,k1+1,k2,k3)
        F(n*3,k1,k2+1,k3)
        F(n+45,k1,k2,k3+1)
kPr=0
F(1,0,0,0)
print(kPr)
    
    
