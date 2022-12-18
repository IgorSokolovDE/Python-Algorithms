def F(n,pred,ok):
    global k
    if n>600: return
    if n==600:
        if ok:
            k+=1
        return
    else:
        if ((n+2)+n+pred)%11==0:
            F(n+2,n,True)
        else:
            F(n+2,n,ok)
        if ((n*3)+n+pred)%11==0:
            F(n*3,n,True)
        else:
            F(n*3,n,ok)
        if ((n*4)+n+pred)%11==0:
            F(n*4,n,True)
        else:
            F(n*4,n,ok)
k=0
F(1,0,False)
print(k)
