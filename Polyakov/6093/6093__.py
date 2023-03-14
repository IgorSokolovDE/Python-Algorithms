f=open('26-102.txt')
N,K=map(int, f.readline().split())
Kont=[]
for i in range(N):
    s=f.readline().split()
    Kont.append([int(s[0]),s[1]])
Kont.sort()
Kont=Kont[::-1]
MaxKolKonBlok=0
KolYachee=0
while len(Kont)>0:
    Blok=[Kont[0]]
    Kont.pop(0)
    prodolPoist=True
    while prodolPoist:
        prodolPoist=False
        for i in range(len(Kont)):
            if Kont[i][1]!=Blok[-1][1]:
                if (Blok[-1][0]-Kont[i][0])>=K:
                    Blok.append(Kont[i])
                    Kont.pop(i)
                    prodolPoist=True
                    break
    MaxKolKonBlok=max(MaxKolKonBlok,len(Blok))
    KolYachee+=1
print(KolYachee, MaxKolKonBlok)   
