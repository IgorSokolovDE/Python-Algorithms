f=open('27-117b.txt')
N,D=map(int, f.readline().split())
UnikCh=[]
SumS=[]
Sum=0
kPodPos=0
for i in range(N):
    x=int(f.readline())
    Sum+=x
    if not(x in UnikCh):
        UnikCh.append(x)
        SumS.append([Sum])
    else:
        num=UnikCh.index(x)
        SumS[num].append(Sum)
for i in range(len(UnikCh)):
    grupa=SumS[i]
    if len(grupa)>1:
        for j in range(len(grupa)-1):
            for k in range(j+1,len(grupa)):
                SumMG=((grupa[k]-UnikCh[i])-grupa[j])
                if(SumMG>0)and(SumMG%D==0):
                    kPodPos+=1
print(kPodPos)                    
        
    
