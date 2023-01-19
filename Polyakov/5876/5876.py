A=[]
for p in range(1,10):
    for y in range(2,300000):
        Yellow=str(y)
        if Yellow[0]=='2':
            if Yellow.count('0')==0:
                s='3'+Yellow+'54'+str(p)+'123'
                if len(s)%2==0:
                    if int(s)%519==0:
                        polov1=s[:len(s)//2]
                        polov2=s[len(s)//2:]
                        SumCifr1=0
                        SumCifr2=0
                        for s1 in polov1: SumCifr1+=int(s1)
                        for s2 in polov2: SumCifr2+=int(s2)
                        if SumCifr1==SumCifr2:
                            A.append(int(s))
                            
A.sort()
for i in range(len(A)): print(A[i],A[i]//519)
