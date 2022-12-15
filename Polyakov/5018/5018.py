def SS5(n):
    S=''
    while n>0:
        S=str(n%5)+S
        n//=5
    return S    
A=[int(x) for x in open('17-278.txt')]
SumVse4=0
for x in A:
    if x%12==0:
        SumVse4+=SS5(x).count("4")*4
print(SumVse4)        
kPar=0
MaxSumElPari=0
for i in range(len(A)-1):
    if (A[i]>SumVse4)and(A[i+1]>SumVse4):
        kPar+=1
        MaxSumElPari=max(MaxSumElPari,(A[i]+A[i+1]))
print(kPar,MaxSumElPari)
