def F(n):
    if n<2:
        return n
    else:
        if n%2==0:
            return F(n//2)+1
        else:
            return F(3*n+1)+1
k=0
for n in range(1,100001):
    if F (n)==16:
        k+=1
    
print(k)
