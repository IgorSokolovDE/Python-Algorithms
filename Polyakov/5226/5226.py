def prost(n):
    pr=True
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            pr=False
            break
    if (n!=1) and pr:
        return True
    else:return False
k=0
kn=0
while kn<5:
    k+=1
    N=19_500_000+k
    if prost(N):
        print(N,1)
        kn+=1
    else:
        for d in range(2,int(N**0.5)+1):
            if N%d==0:
                break
                
        if prost(N//d):
            print(k,N//d)
            kn+=1
