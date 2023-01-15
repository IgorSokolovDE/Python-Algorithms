f=open('27-101b.txt')
N=int(f.readline())
A=[int(x) for x in f]
K=0
for i in range(N):
    pr=1
    for j in range(i,N):
        pr*=A[j]
        if pr%858967==0:
            break
        else:
            K+=1
print(K)            
    
