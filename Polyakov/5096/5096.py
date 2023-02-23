def F(n,k):
    if k==11:
        if n<0:
            if not(n in Res):
                Res.append(n)
        return
    else:
        F(n-2,k+1)
        F(n*(-3),k+1)
Res=[]
F(91,0)
print(len(Res))
