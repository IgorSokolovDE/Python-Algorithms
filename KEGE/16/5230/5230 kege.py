def F(n,k):
    if k==0:
        return 0
    else:
        if n%k==0:
            return F(n,k-1)+k*k
        else:
            return F(n,k-1)
for k in range(1,26):
    print(k, F(100, k))   
