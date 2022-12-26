f=open('27-97b.txt')
n,k=map(int, f.readline().split())
kolOst=[0]*k
kolOst[0]=1
Sum=0
for i in range(n):
    Sum+=int(f.readline())
    kolOst[Sum%k]+=1
kolPodPos=0
for i in range(k):
    kolPodPos+=(kolOst[i]*(kolOst[i]-1))//2
print(kolPodPos)    
