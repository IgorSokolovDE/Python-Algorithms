k=0
while k*9797<10**7:
    k+=1
    Ch=k*9797
    ChS=str(Ch)
    if (ChS[0]=='3')and(ChS[-1]=='1'):
        P=int(ChS[1:-1])
        prost=True
        for d in range(2,int(P**0.5)+1):
            if P%d==0:
                prost=False
                break
        if prost:
            print(Ch,k)
