def F(n,KinNeCh):
    global k
    if n>35:
        return
    if n==35:
        if KinNeCh<=2:
            k+=1
        return
    else:
        F(n+2,KinNeCh)
        if n%2!=0:
            F(n*2,KinNeCh)
        else:
            F(n*2+1,KinNeCh+1)
k=0
F(2,0)
print(k)
