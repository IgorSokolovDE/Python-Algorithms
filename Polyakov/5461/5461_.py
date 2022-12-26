f=open('26-95.txt')
N=int(f.readline())
Jalobi=[]
for i in range(N):
    d,p=map(int, f.readline().split())
    Jalobi.append([d,p])
Jalobi.sort()
Dom=Jalobi[0][0]
obr=[]
kolRemDom=0
for i in range(N):
    if Jalobi[i][0]==Dom:
        obr.append(Jalobi[i][1])
    else:
        
        if len(obr)>=3:
            DomRem=False
            for pBezJalob in range(obr[0]-1,obr[-1]+2):
                if not(pBezJalob in obr):
                    kpsosedjalob=0
                    ppravo=pBezJalob+1
                    while ppravo in obr:
                        kpsosedjalob+=1
                        ppravo+=1
                    plevo=pBezJalob-1
                    while plevo in obr:
                        kpsosedjalob+=1
                        plevo-=1    
                    if kpsosedjalob>=3:
                        DomRem=True
                        break
            if DomRem:
                 kolRemDom+=1
                 MinP=pBezJalob
                 
                
        
        Dom=Jalobi[i][0]
        obr=[Jalobi[i][1]]
print(kolRemDom, MinP)       
