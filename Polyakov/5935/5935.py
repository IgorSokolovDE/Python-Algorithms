f=open('26-98.txt')
N,S=map(int, f.readline().split())
Tovari=[]
for i in range(N):
    s=f.readline()
    a=s.split()
    CenaBesSkidki=int(a[0])
    if len(a[1])==1:
        Cena=CenaBesSkidki
        kategor=a[1]
    else:
        kategor=a[1]
        if kategor[0]=="A":
            Cena=CenaBesSkidki*0.9
        else:
            Cena=CenaBesSkidki*0.8
    Tovari.append([Cena,CenaBesSkidki, kategor])
Tovari.sort()
SumDENEG=0
kupili=[]
SumKupleno=0
maxkolTovarov=0
for i in range(N):
    SumDENEG+=Tovari[i][0]
    if SumDENEG>S:
        break
    else:
       SumKupleno +=Tovari[i][0]
       kupili.append(Tovari[i]) 
       maxkolTovarov+=1
print(SumKupleno,end=' ')
predCena=S-(SumKupleno-kupili[-1][0])
for j in range(i-1,N):
    if (Tovari[j][0]<=predCena)and(Tovari[j][0]!=Tovari[j][1]):
        Max=Tovari[j][0]
print(Max)        
