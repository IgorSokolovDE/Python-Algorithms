# A=[int(x) for x in open('17-333.txt')]
A=[]
f=open('17-333.txt')
while True:
    s=f.readline()
    if not(s):
        break
    A.append(int(s))
Sum4=0
kol4=0
kPar=0
MaxSumCifr=0
for x in A:
    if 1000<=x<=9999:
        Sum4+=x
        kol4+=1
AVG4=Sum4/kol4
for i in range(len(A)-1):
    SumPari=A[i]+A[i+1]
    if not(SumPari in A):
        if SumPari<AVG4:
            kPar+=1
            SumCifr=0
            ParaS=str(A[i])+str(A[i+1])
            for sym in ParaS:
                SumCifr+=int(sym)
            MaxSumCifr=max(MaxSumCifr,SumCifr)
print(kPar, MaxSumCifr)            
