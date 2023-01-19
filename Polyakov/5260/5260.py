A=[int(x) for x in open('17-332.txt')]
Sum17=0
kol17=0
k3=0
ASumCifr2=[]
KolSumCifr2=[]
for x in A:
    if x%17==0:
        Sum17+=x
        kol17+=1
avg17=Sum17/kol17
for i in range(len(A)-2):
    if A[i+1]<avg17:
        SumCifr1=0
        x=(A[i])
        while x>0:
            SumCifr1+=(x%10)
            x//=10
        SumCifr3=0
        x=(A[i+2])
        while x>0:
            SumCifr3+=(x%10)
            x//=10
        SumCifr2=0
        x=(A[i+1])
        while x>0:
            SumCifr2+=(x%10)
            x//=10    
        if SumCifr1==SumCifr3:
            k3+=1
            if not(SumCifr2 in ASumCifr2):
                ASumCifr2.append(SumCifr2)
                KolSumCifr2.append(1)
            else:
                num=ASumCifr2.index(SumCifr2)
                KolSumCifr2[num]+=1
num=KolSumCifr2.index(max(KolSumCifr2))
print(k3,ASumCifr2[num])
            
        
