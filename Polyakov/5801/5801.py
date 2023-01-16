A=[int(x) for x in open('17-346.txt')]
k3=0
MaxPr=0
for i in range(len(A)-2):
    S=str(A[i])+str(A[i+1])+str(A[i+2])
    prCifr=1
    for Cifr in S:
         prCifr*=int(Cifr)
    if (prCifr<(2*10**9))and((prCifr>=100)):
        SprCifr=str(prCifr)
        if SprCifr[:2]=='55':
            if '2' in SprCifr[2:]:
                k3+=1
                MaxPr=max(MaxPr,prCifr)
print(k3,MaxPr)                
        
