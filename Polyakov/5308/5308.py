f=open('26-86.txt')
N=int(f.readline())
BLUDI=[]
for i in range(N):
    time,kod=map(int, f.readline().split())
    BLUDI.append([time,kod])
BLUDI.sort()
gotovoeBludo=[]
TimeGotovli=[]
for i in range(len(BLUDI)):
    if BLUDI[i][1] in gotovoeBludo:
        num=gotovoeBludo.index(BLUDI[i][1])
        TimeGotovli[num].append(BLUDI[i][0])
    else:
        gotovoeBludo.append(BLUDI[i][1])
        TimeGotovli.append([BLUDI[i][0]])
MaxAvgTime=0
AllTime=[]
VsegoZakazov=0
for i in range(len(gotovoeBludo)):
    j=0
    SumTimeZakaza=0
    kolZakazov=0
    while j<len(TimeGotovli[i]):
        if (j+1)<len(TimeGotovli[i]):
           SumTimeZakaza+= TimeGotovli[i][j+1]-TimeGotovli[i][j]
           AllTime.append([TimeGotovli[i][j],TimeGotovli[i][j+1]])
           kolZakazov+=1
           j+=2
           
        else:
            break
    if kolZakazov!=0:
        VsegoZakazov+=kolZakazov
        avgTime= SumTimeZakaza/kolZakazov
        if (MaxAvgTime<avgTime):
            MaxAvgTime=avgTime
            NumMax=i
AllTime.sort()
MaxkolBludVChas=0
for i in range(len(AllTime)):
    kolBludVChas=0
    bludVchas=[]
    konec=AllTime[i][0]+60
    for j in range(i,len(AllTime)):
        if AllTime[j][1]<=konec:
            kolBludVChas+=1
            bludVchas.append(AllTime[j])
    #print(kolBludVChas,len(bludVchas),konec)
    #print(bludVchas)
    #iii=input()
    MaxkolBludVChas=max(MaxkolBludVChas,kolBludVChas)        
print(MaxkolBludVChas,gotovoeBludo[NumMax])    
        
    
        
                   
               
