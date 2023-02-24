for N in range(248456785,248456795):
    N2=bin(N)[2:]
    N10=int(N2,2)
    SumCifr=0
    while N10>0:
        SumCifr+=N10%10
        N10//=10
    if  SumCifr%2==1:
        N2=N2+'1'
    else:
        N2=N2+'0'
    N10=int(N2,2)
    SumCifr=0
    while N10>0:
        SumCifr+=N10%10
        N10//=10
    if  SumCifr%2==1:
        N2=N2+'1'
    else:
        N2=N2+'0'
    N10=int(N2,2)
    SumCifr=0
    while N10>0:
        SumCifr+=N10%10
        N10//=10
    if  SumCifr%2==1:
        N2=N2+'1'
    else:
        N2=N2+'0'
    R=int(N2,2)
    print(N,R,R/N)
    
