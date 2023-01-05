f=open('26-93.txt')
N,M= map(int, f.readline().split())
TC=[]
PodMest=0
MaxEtash=0
for i in range(N):
    etasch,mesto= map(int, f.readline().split())
    TC.append([etasch,mesto])
TC.sort()
etash=[]
NumEtash=TC[0][0]
for i in range(N):
    if NumEtash==TC[i][0]:
        etash.append(TC[i][1])
    else:
        #анализировать какие места в пройденом этаже
        if len(etash)>1:
            #ищем свободные места
            if etash[0]>1:
                StMesto=etash[0]-1
            else:
                StMesto=2    
            for nummesta in range(StMesto,etash[-1]+1):
                if not(nummesta in etash):
                    kolvikupl=0
                    provM=nummesta+1
                    while provM in etash:
                        kolvikupl+=1
                        provM+=1
                    provM=nummesta-1
                    while provM in etash:
                        kolvikupl+=1
                        provM-=1
                    if  kolvikupl>=M:
                        PodMest+=1
                        MaxEtash=max(MaxEtash,NumEtash)
                    
            
        NumEtash=TC[i][0]
        etash=[]
        etash.append(TC[i][1])
print(PodMest,MaxEtash)        
    
    
