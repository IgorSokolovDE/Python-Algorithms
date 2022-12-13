f=open('26-92.txt'); Ekran=[]
for i in range(10001):
    Stroka=[]
    for j in range(10001):
        Stroka.append('-')
    Ekran.append( Stroka)   
N=int(f.readline())
while True:
    s=f.readline()
    if not(s): break
    a=s.split()
    x=int(a[0])-1 ; y=int(a[1])-1
    znak=a[2]; Ekran[x][y]=znak
MaxPos=0
for i in range(10001):
    Stroka=Ekran[i]; kPos=0
    for j in range(10001):
        if (Stroka[j]=='+') and (Stroka[j+1]=='+'):
            if kPos==0:
                kPos=2
            else:
                kPos+=1
                if kPos>=MaxPos:  #нужен знак >="
                    MaxPos=kPos
                    SStroka=i
        else:
          kPos=0
print(MaxPos, SStroka+1) #+1 потому то у нас номер строки начинается с 0,а
                         #в задаче с 1         


