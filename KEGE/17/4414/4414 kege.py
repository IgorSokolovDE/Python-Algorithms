A=[int(x) for x in open('17 (1).txt')]
kPar=0
MaxR=0
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        R=abs(A[i]-A[j])
        if R%36==0:
            if (A[i]%13==0) or( A[j]%13==0):
                kPar+=1
                MaxR=max(MaxR,R)
print(kPar,MaxR)                
        
