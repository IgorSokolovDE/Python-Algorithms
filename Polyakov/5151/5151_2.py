x=8_023_320
MN=[1]
d=2
while x!=1:
    if x%d==0:
        MN.append(d)
        x=x//d
    else:
        d+=1
print(MN)
f=open('27-106b.txt')
N=int(f.readline())
a=[]
MaxKEPodPos=0
for i in range(N):
    a.append(int(f.readline()))
for start in range(N):
    MNS=MN[:]
    KEPodPos=0
    ok=True
    for i in range(start,N):
        x=a[i]
        d=2
        while x!=1:
            if x%d==0:
                if not(d in MNS):
                    ok=False
                    break
                else:
                    index=MNS.index(d)
                    MNS.pop(index)
                x=x//d    
            else:
                d+=1
        if not(ok):
            break
        else:
            KEPodPos+=1
    if KEPodPos>MaxKEPodPos:
        MaxKEPodPos=KEPodPos
        Num=start
print(Num+1,MaxKEPodPos)        
                
