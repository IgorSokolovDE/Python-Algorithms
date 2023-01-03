for M in range(1,1000000000000000000000000):
    p1=2
    p2=1
    S=str(M)
    for sym in S:
        if (int(sym))%2==1:
            p2=p2*int(sym)
        else:
            if (int(sym))>0:
                p1=p1*int(sym)
    R=abs(p1-p2)
    if R==29:
        print(M)
        break
