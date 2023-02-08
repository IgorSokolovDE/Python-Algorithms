def f(n,kolChsumcifr14):
    global kPr
    if n>600: return
    if n==600:
        if kolChsumcifr14==5:
            kPr+=1
        return
    else:
        SumCifr=0
        x=n+2
        while x>0:
            SumCifr+=(x%10)
            x//=10
        if SumCifr==14:
            f(n+2,kolChsumcifr14+1)
        else:
            f(n+2,kolChsumcifr14)
        SumCifr=0
        x=n*3
        while x>0:
            SumCifr+=(x%10)
            x//=10
        if SumCifr==14:
            f(n*3,kolChsumcifr14+1)
        else:
            f(n*3,kolChsumcifr14)
        SumCifr=0
        x=n*4
        while x>0:
            SumCifr+=(x%10)
            x//=10
        if SumCifr==14:
            f(n*4,kolChsumcifr14+1)
        else:
            f(n*4,kolChsumcifr14)      
kPr=0
f(1,0)
print(kPr)
