f=open('26-96.txt')
N=int(f.readline())
Dolgota=[]
KolSign=[]
Signals=[]
for i in range(N):
    Schir,Dolg = map(int, f.readline().split())
    Signals.append([int(Schir/10),Dolg])
    if Dolg in Dolgota:
        numPos=Dolgota.index(Dolg)
        KolSign[numPos]+=1
    else:
        Dolgota.append(Dolg)
        KolSign.append(1)
numMKol=KolSign.index(max(KolSign))
D=Dolgota[numMKol]
SchirNew=[]
KolSign2=[]
for i in range(N):
    if Signals[i][1]==D:
        if Signals[i][0] in SchirNew:
            numPos=SchirNew.index(Signals[i][0])
            KolSign2[numPos]+=1
        else:
            SchirNew.append(Signals[i][0])
            KolSign2.append(1)
print(D,len(KolSign2))

    
