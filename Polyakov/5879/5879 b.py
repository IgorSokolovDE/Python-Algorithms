f=open('27-129b.txt')
N=int(f.readline())
A=[]
ost13=[]
for i in range(13): ost13.append([])
Sum=0
for i in range(N):
    x=int(f.readline())
    Sum+=x
    A.append(Sum)
    ost13[Sum%13].append(i)
f=open('27-129b.txt')
N=int(f.readline())
for i in range(N,2*N):
    x=int(f.readline())
    Sum+=x
    A.append(Sum)
    ost13[Sum%13].append(i)
f=open('27-129b.txt')
N=int(f.readline())
for i in range(2*N,3*N):
    x=int(f.readline())
    Sum+=x
    A.append(Sum)
    ost13[Sum%13].append(i)    
MaxSumPos=0
for i in range(13):
    for j in range(len(ost13[i])-1,0,-1):
        for k in range(j):
            if ((ost13[i][j]-ost13[i][k])%13==0)and((ost13[i][j]-ost13[i][k])<=N):
         
                MaxSumPos=max((A[ost13[i][j]]-A[ost13[i][k]]),MaxSumPos)                
                break
print(MaxSumPos)                
    
