def F(n):
    if n==0: return 1
    else:
        return 7*(n-1)+F(n-1)
kprost=0
for n in range(2,201):
    x=F(n)
    prost=True
    for d in range(2,int(x**0.5)+1):
        if x%d==0:
            prost=False
            break
    if prost:
        kprost+=1
print(kprost)        
