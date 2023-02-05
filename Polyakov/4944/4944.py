A=[]
N=400_000_000
kn=0
while kn<5:
    N+=1
    OsobDel=[]
    for d in range(2,int(N**0.5)+1):
        if N%d==0:
            SumCifr=0
            s=str(d)
            for s1 in s:
                SumCifr+=int(s1)
            if  SumCifr==20:
                OsobDel.append(d)
            if d*d != N:
                SumCifr=0
                s=str(N//d)
                for s1 in s:
                    SumCifr+=int(s1)
                if  SumCifr==20:
                    OsobDel.append(N//d)
    if len( OsobDel)>=6:
         OsobDel.sort()
         OsobDel=OsobDel[::-1]
         print(OsobDel[5],len(OsobDel))
         kn+=1


         
                
