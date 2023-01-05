A=[int(x) for x in open('17.txt')]
Min5=10000000000000000000000000000
for x in A:
    if (abs(x)%10)==5:
        Min5=min(Min5,x)
kPar=0
MaxSumKv=0
for i in range(len(A)-1):
    minVpare=min(A[i],A[i+1])
    if minVpare%10==5:
        if (A[i]**2+A[i+1]**2)<(Min5**2):
            kPar+=1
            MaxSumKv=max((A[i]**2+A[i+1]**2),MaxSumKv)
print(kPar,MaxSumKv)            
            
