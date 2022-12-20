A=[]
k=62
while k*161<=17*10**6:
    k+=1
    Ch=k*161
    Chs=str(Ch)
    if ('1' in Chs)and('68' in Chs):
        num1=Chs.index('1')
        ChsNAOBOROT=Chs[::-1]
        num86=ChsNAOBOROT.index('86')
        num68=len(Chs)-num86-2
        if (num68-num1-1)>=2:
            A.append(Ch)
for i in range(0,len(A),500):
    print(A[i],A[i]//161)
        
