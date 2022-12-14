A=[int(x) for x in open('17-344.txt')]
minKr103=1000000000000000000000000000
for x in A:
    if x%103==0:
        minKr103=min(minKr103,x)
kPar=0
MaxSumElPari=0
for i in range(len(A)-1):
    if (A[i]+A[i+1])%2==0:
        if (abs(A[i]-A[i+1]))%minKr103==0:
            kPar+=1
            MaxSumElPari=max(MaxSumElPari,(A[i]+A[i+1]))
print(kPar,MaxSumElPari)        
