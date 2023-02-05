A=[int(x) for x in open('17-342.txt')]
min37=10000000000000000000000000000000
max73=0
for x in A:
    if x%37==0:
        min37=min(min37,x)
    if x%73==0:
        max73=max(max73,x)

kPar=0
minSum=100000000000000000000000000000
for i in range(len(A)-1):
    if ((max73<A[i]<min37)and not(max73<A[i+1]<min37)) or\
       ((max73<A[i+1]<min37)and not(max73<A[i]<min37)) :
        kPar+=1
        minSum=min(minSum,(A[i]+A[i+1]))
       
print(kPar,minSum)
