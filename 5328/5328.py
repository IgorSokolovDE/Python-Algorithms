A=[int(x) for x in open('17-338.txt')]
M=min(A)
kpar=0
MaxS=0
for i in range(len(A)-1):
    if ((A[i]%117)==M)or((A[i+1]%117)==M):
        kpar+=1
        MaxS=max(MaxS,(A[i]+A[i+1]))
print(kpar,MaxS)        
