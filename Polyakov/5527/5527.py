A=[int(x) for x in open('17-345.txt')]
Min52=100000000
Max52=0
for x in A:
    if x%100==52:
        Min52=min(x,Min52)
        Max52=max(x,Max52)
Razn=Max52-Min52        
kPar=0
MaxSumElPari=0
for i in range(len(A)-1):
    if ((A[i]<Razn)and(A[i+1]>=Razn))or\
       ((A[i+1]<Razn)and(A[i]>=Razn)):
        kPar+=1
        MaxSumElPari=max(MaxSumElPari,(A[i]+A[i+1]))
print(kPar,MaxSumElPari)        
        
