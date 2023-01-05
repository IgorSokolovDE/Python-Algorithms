N=60000
kn=0
while kn<5:
    N+=1
    prost=True
    D=1
    for d in range(2,int(N**0.5)+1):
        if N%d==0:
            prost=False
            D=N//d
            break
    Mn=[]
    x=N; d=2
    while x>1:
        if x%d==0:
            Mn.append(d)
            x=x//d
        else:
            d+=1
    S=str(sum(Mn))
    S=S[::-1]
    Q=int(S)
    if N+D+Q>202122:
        print(N,D+Q)
        kn+=1
        
    
