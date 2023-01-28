A=[int(x) for x in open('17-335.txt')]
M=100000000000
k2=0
Max=0
for x in A:
    if x%43==0:
        M=min(M,x)
for i in range(len(A)-1):
    if ((A[i]+A[i+1])% M==0)or((A[i]%10)==(M%10))or((A[i+1]%10)==(M%10)):
        k2+=1
        Max=max(Max,A[i],A[i+1])
print(k2,Max)        
