f=open('24-235.txt')
MaxL=0
SymMaxkol=0
sym=''
MaxkolB=0
while True:
    s=f.readline()
    if not(s):
        break
    L=''
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            if len(L)==0:
                L=s[i]+s[i+1]
            else:
                L+=s[i+1]
        else:
            
            
            for kod in range(65,91):
                if L.count(chr(kod))>MaxkolB:
                    MaxkolB=L.count(chr(kod))
               
            L=''
    if  MaxkolB  >= SymMaxkol:
        SymMaxkol=MaxkolB
print(SymMaxkol)        
