kVar=0
for x in range(0,2**11):
    x2=bin(x)[2:]
    x2='0'*(11-len(x2))+x2
    if x2.count('1')==4:
        if not('11' in x2):
           if x2[0]=='0':
               kVar+=3*4**10
           else:
               kVar+=4**11
print(kVar)               
