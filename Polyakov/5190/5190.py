A=[int(x) for x in open('17-304.txt')]
M246=0
kpar=0
MaxSum=0
for x in A:
    if x%246==0:
        M246=max(M246,x)
for i in range(len(A)-1):
    if ('aa' in (hex(A[i])[2:]))and('aa' in (hex(A[i+1])[2:])):
        if (A[i]+A[i+1])<M246:
            kpar+=1
            MaxSum=max(MaxSum,(A[i]+A[i+1]))
print(kpar,MaxSum)            
