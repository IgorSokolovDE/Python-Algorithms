f=open('26-j2.txt')
N=int(f.readline())
A=[int(x) for x in f]
A.sort()
Mediana=A[N//2]
Sr=sum(A)/N
k=0
for i in range(N//2,0,-1):
    if (A[i]<=Mediana)and(A[i]>=Sr):
        k+=1
    else:
        break
for i in range(N//2+1,N):
    if (A[i]<=Mediana)and(A[i]>=Sr):
        k+=1
    else:
        break    
print(k)    
                          
    
