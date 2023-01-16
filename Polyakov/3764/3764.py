f=open('26-48.txt')
kPar=0
MinAVG=100000000000000000000000
N=int(f.readline())
A=[int(x) for x in f]
A.sort()
for i in range(N-1):
    for j in range(i+1,N):
        if (A[i]+A[j])%2==0:
            avg=(A[i]+A[j])//2
            MinK=100000000000000000000000
            for m in range(N):
               MinK=min(abs(A[m]-avg),MinK)
            if MinK==5:
                kPar+=1
                MinAVG=min(MinAVG,avg)
print(kPar,MinAVG)               
            
