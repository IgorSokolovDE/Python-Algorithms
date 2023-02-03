abc=[]
for i in range(65,91):
    abc.append(chr(i))
VsegoGl=0    
for a in abc:
    for b in abc:
        for c in abc:
            for d in abc:
                for e in abc:
                    slovo=a+b+c+d+e
                    VsegoGl+=slovo.count('A')
                    VsegoGl+=slovo.count('E')
                    VsegoGl+=slovo.count('I')
                    VsegoGl+=slovo.count('O')
                    VsegoGl+=slovo.count('U')
                    VsegoGl+=slovo.count('Y')
print(VsegoGl)                    

            
    
