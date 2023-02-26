MinR=10000000000000000000000
for N in range(1000,10000):
    A=[]
    x=N
    while x>0:
        A.append(x%10)
        x//=10
    A=A[::-1]
    if N%2==0:
        A.sort()
        A=A[::-1]
        NewN=A[0]*1000+A[1]*100+A[2]*10+A[3]
        R=NewN//2
    else:
        A.sort()
        NewN=A[0]*1000+A[1]*100+A[2]*10+A[3]
        R=NewN*2
    if (R-N)==1:
        MinR=min(MinR,R)
    
print(MinR)

