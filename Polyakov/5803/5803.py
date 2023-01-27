A=[int(x) for x in open('17-346.txt')]
kolTR=0
MaxPrVsehCifr=0
for i in range(len(A)-2):
    PrCh=1
    PrVseh=1
    x=A[i]
    while x>0:
        if (x%10)%2==0:
            PrCh*=x%10
        PrVseh*=x%10
        x=x//10
    x=A[i+1]
    while x>0:
        if (x%10)%2==0:
            PrCh*=x%10
        PrVseh*=x%10
        x=x//10
    x=A[i+2]
    while x>0:
        if (x%10)%2==0:
            PrCh*=x%10
        PrVseh*=x%10
        x=x//10
    if  (PrCh<=2*10**9) :
        S=str(PrCh)
        if len(S)>=3:
            if S[:2]=='25':
                if ('2' in S[2:]):
                    kolTR+=1
                    MaxPrVsehCifr=max(MaxPrVsehCifr,PrCh)
print(kolTR, MaxPrVsehCifr)                   
        
