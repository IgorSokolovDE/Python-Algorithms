f=open('24-247.txt')
MaxL=0
BukvaL=''
KolBukvav=0
while True:
    s=f.readline()
    if not(s):
        break
    L=0
    for i in range(len(s)-1):
        if s[i]== s[i+1]:
            if L==0:
                L=2
            else:
                L+=1
        else:
            if L>MaxL:
                MaxL=L
                BukvaL=s[i]
                KolBukvav=s.count(s[i])
            else:
                if L==MaxL:
                    if s.count(s[i])<KolBukvav:
                        BukvaL=s[i]
                        KolBukvav=s.count(s[i])
            L=0            
print(KolBukvav)                        
                
