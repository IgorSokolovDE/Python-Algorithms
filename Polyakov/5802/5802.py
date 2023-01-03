A=[int(x) for x in open('17-346.txt')]
kTr=0
MaxPrCifr=0
for i in range(len(A)-2):
    s=str(A[i])+str(A[i+1])+str(A[i+2])
    prCifr=1
    for sym in s:
        prCifr=prCifr*int(sym)
    if (prCifr<=2*10**9):
        SprCifr=str(prCifr)
        if (SprCifr[:2]=='83')and('8' in SprCifr[2:]):
            kTr+=1
            MaxPrCifr=max(MaxPrCifr,prCifr)
print(kTr,MaxPrCifr)            
