A=[int(x) for x in open('17-346.txt')]
k3=0
MaxPrCifr=0
for i in range(len(A)-2):
    s=str(A[i])+str(A[i+1])+str(A[i+2])
    PrCifr=1
    for cifra in s: PrCifr=PrCifr*int(cifra)
    if (PrCifr<=2*10**9)and(PrCifr>100):
        sPrCifr=str(PrCifr)
        if (sPrCifr[:2]=='53')and('7' in sPrCifr[2:]):
            k3+=1
            MaxPrCifr=max(MaxPrCifr,PrCifr)
print(k3,MaxPrCifr)            
        
