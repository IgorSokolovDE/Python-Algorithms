N=520000
kn=0
while kn<5:
    N+=1
    NeTrDel=[]
    for d in range(2,int(N**0.5)+1):
        if N%d==0:
            NeTrDel.append(d)
            if d**2!=N:
                NeTrDel.append(N//d)
    if len(NeTrDel)>0:            
        S=str(sum(NeTrDel))
        if (S==S[::-1])and (len(S)>0):
            print(N,max(NeTrDel))
            kn+=1
              
