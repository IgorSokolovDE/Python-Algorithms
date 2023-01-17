f=open('26-97.txt')
N=int(f.readline())
trubi=[]
for i in range(N):
    D,S=map(int, f.readline().split())
    trubi.append([D,S])
trubi.sort()
i=0
while i<len(trubi)-1:
    if (trubi[i][0]==trubi[i+1][0]):
        trubi.pop(i+1)
    else:
        i+=1      
MaxKolVpakete=0
for j in range(len(trubi)):
    Paket=[]
    Paket.append(trubi[j])
    for i in range(j,len(trubi)):
        if (trubi[i][0]-2*trubi[i][1]-3)>=Paket[-1][0]:
            Paket.append(trubi[i])
    if MaxKolVpakete<len(Paket):
        MaxKolVpakete=len(Paket)
        MaxDMinTrubi=Paket[0][0]
    else:
        if MaxKolVpakete==len(Paket):
           if MaxDMinTrubi< Paket[0][0]:
               MaxDMinTrubi= Paket[0][0]
print(MaxKolVpakete,MaxDMinTrubi)

