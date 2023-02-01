kVar=0
for x in range(2**10):
    x2=bin(x)[2:]
    x2='0'*(10-len(x2))+x2
    if 1 < x2.count('1') < 6:
        vSgl=21
        vGl=5
        pr=1
        for s in x2:
            if s=='0':
                pr*=vSgl
                vSgl-=1
            else:
                pr*=vGl
                vGl-=1
        kVar+=pr
SumCifr=0
while(kVar>0):
    SumCifr+=kVar%10
    kVar//=10
print(SumCifr)    
