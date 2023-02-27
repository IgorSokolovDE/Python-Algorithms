MinR=1000000000000000000000000000000
N10=0
for N in range(64,10000):
    N2=bin(N)[2:]
    if N2.count('1')%2==0:
        inver=N2[-4:]
        neizm=N2[:-4]
        inver= inver.replace('0','*')
        inver= inver.replace('1','0')
        inver= inver.replace('*','1')
        NewN2=(neizm+inver)
    else:
        inver=N2[-5:-1]
        neizm1=N2[:-5]
        neizm2=N2[-1]
        inver= inver.replace('0','*')
        inver= inver.replace('1','0')
        inver= inver.replace('*','1')
        NewN2=(neizm1+inver+neizm2)
    R=int(NewN2,2)
    if R<MinR:
        MinR=R
        N10=N
print(N10)        
