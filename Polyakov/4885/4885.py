def F(n):
    if n<=1:
        return 1
    else:
        if n%2==0:
            return 11*n+F(n-1)
        else:
            return 11*F(n-2)+n
SumCh=0        
for n in range(35,51):
    Ch=F(n)
    if Ch%2==0:
        SumCh+=Ch
print(len(str(SumCh)))        
        
