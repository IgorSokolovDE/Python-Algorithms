def F(n,k):
    global kpr
    print(n)
    ii=input()
    if n>45789:
        return
    if n==45789:
        kpr+=1
        print('!')
        return
    else:
        if k==0:
            F(n+1,1)
            F(n*2,2)
            F(n+3,3)
        else:
            if k==1:
                F(n*2,2)
                F(n+3,3)
            else:
                if k==2:
                     F(n+1,1)
                     F(n+3,3)
                else:
                    F(n+1,1)
                    F(n*2,2)
kpr=0
F(5001,0)
print(kpr)
