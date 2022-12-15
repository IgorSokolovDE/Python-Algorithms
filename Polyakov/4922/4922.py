f=open('27-97b.txt')
#N,K= map(int, f.readline().split())
s=f.readline()
a=s.split()
N=int(a[0])
K=int(a[1])
A=[0]*K
A[0]=1
Sum=0
for i in range(N):
    x=int(f.readline())
    Sum+=x
    A[Sum%K]+=1
kolPodPos=0    
for i in range(K): kolPodPos+=(A[i]*(A[i]-1))//2
print(kolPodPos)
    
