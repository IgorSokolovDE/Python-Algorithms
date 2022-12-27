A=[int(x) for x in open('17-336.txt')]
M=100000000000000000000000000000000000
for x in A:
    if (x%8==0)and(x!=8):
        M=min(M,x)
KPar=0
MinEl=[1111111111,11111111111111111]
for i in range(len(A)-1):
    if (A[i]%M==0)and(A[i+1]%M==0):
        KPar+=1
        if (A[i]+A[i+1])<sum(MinEl):
            MinEl[0]=max(A[i],A[i+1])
            MinEl[1]=min(A[i],A[i+1])
print(KPar,MinEl[0])        
