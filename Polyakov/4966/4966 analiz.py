def F(n):
    if n==0: return 1
    else:
        if n%2!=0:
            return(1+F(n-1))
        else:
            return F(n//2)
for n in range(1,100):
    print(n,bin(n)[2:],F(n))
