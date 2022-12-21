def F(n,pred):
    global k
    if n>27: return
    if n==27:
        k+=1
        return
    else:
        F(n+1,n)
        F(n*3,n)
        if pred>0:
            F(n+pred,n)
k=0
F(2,0)
print(k)
