kolVar=0
k=0
for x in range(2**10):
    x2=bin(x)[2:]
    x2_10='0'*(10-len(x2))+x2
    if (x2_10.count('1')>=2):
        if (x2_10.count('1')<=5):
            Pr=1
            varSgl=21
            varGl=5
            for s in x2_10:
                if s=='0':
                    Pr=Pr*varSgl
                    varSgl=varSgl-1
                else:
                    Pr=Pr*varGl
                    varGl=varGl-1
           
            kolVar=kolVar+Pr
print(kolVar)        
    
