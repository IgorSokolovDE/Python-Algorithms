N=800000
kn=0
while kn<6:
    N+=1
    Del=[]
    for d in range(1,int(N**0.5)+1):
        if N%d==0:
            Del.append(d)
            if d*d !=N:
                Del.append(N//d)
    if len(Del)>10:
        if sum(Del)%2!=0:
            pr=1
            for d in Del:
                pr*=d
            if pr%2 !=0:
                print(N,len(Del))
                kn+=1
                
