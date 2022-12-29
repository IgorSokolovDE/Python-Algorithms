A =[]
for i in range(4):
    rad=[]
    for j in range(9): rad.append(0)
    A.append(rad)
f=open('27-A.txt')
N=int(f.readline())
for i in range(N):
    x=int(f.readline())
    ost4=x%4
    k3=0
    while x%3==0:
        k3+=1
        x//=3
    if k3>8: k3=8    
    A[ost4][k3]+=1
kPar=0
i=0
for j in range(4):
    for k in range(8-j,9):
        kPar+=A[0][j]*A[0][k]
for j in range(4,8):       
    kPar+= (A[0][j]*(A[0][j]-1))//2
    for k in range(j+1,9):
        kPar+=A[0][j]*A[0][k]
kPar+= (A[0][8]*(A[0][8]-1))//2        
i=1
for j in range(9):
    for k in range(8-j,9):
        kPar+=A[1][j]*A[3][k]
i=2
for j in range(4):
    for k in range(8-j,9):
        kPar+=A[2][j]*A[2][k]
for j in range(4,8):       
    kPar+= (A[2][j]*(A[2][j]-1))//2
    for k in range(j+1,9):
        kPar+=A[2][j]*A[2][k]
kPar+= (A[2][8]*(A[2][8]-1))//2           
print(kPar)    
