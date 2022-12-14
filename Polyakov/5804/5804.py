def PrCh(n):
    pr=1
    while n>0:
        if (n%10)%2==0:
            pr*=n%10
        n//=10
    return pr    
kTr=0
Maxpr3Ch=0
A=[int(x) for x in open('17-346.txt')]
for i in range(len(A)-2):
    pr3Ch=(PrCh(A[i])*PrCh(A[i+1])*PrCh(A[i+2]))
    if pr3Ch<2*10**9:
        if pr3Ch>100:
            s=str(pr3Ch)
            if s[:2]=='11':
                if ('6' in s[2:]):
                    kTr+=1
                    Maxpr3Ch=max(Maxpr3Ch,pr3Ch)
print(kTr,Maxpr3Ch)                    
    
